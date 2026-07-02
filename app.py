import os
import uuid
from datetime import datetime

from flask import (
    Flask, render_template, redirect, url_for, flash, request, jsonify, session
)
from flask_login import (
    LoginManager, login_user, logout_user, login_required, current_user
)
from werkzeug.utils import secure_filename

from config import Config
from models import db, User, Module, QuizQuestion, Riddle, Progress
from forms import (
    RegisterForm, LoginForm, UpdateUsernameForm, UpdatePasswordForm, UpdatePhotoForm,
    SecurityQuestionForm, ForgotPasswordForm, ResetPasswordForm
)
from content import MODULES


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "login"
    login_manager.login_message_category = "info"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    def allowed_file(filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

    def get_or_create_progress(user, module_id):
        prog = Progress.query.filter_by(user_id=user.id, module_id=module_id).first()
        if not prog:
            prog = Progress(user_id=user.id, module_id=module_id)
            db.session.add(prog)
            db.session.commit()
        return prog

    def module_unlocked(user, module_order):
        return module_order <= user.highest_unlocked_module()

    @app.route("/")
    def index():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        return render_template("index.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        form = RegisterForm()
        if form.validate_on_submit():
            user = User(username=form.username.data.strip(), email=form.email.data.strip().lower())
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Account created. You can now log in.", "success")
            return redirect(url_for("login"))
        return render_template("register.html", form=form)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data.strip()).first()
            if user and user.check_password(form.password.data):
                user.update_streak()
                db.session.commit()
                login_user(user, remember=form.remember.data)
                flash(f"Welcome back, {user.username}!", "success")
                next_page = request.args.get("next")
                return redirect(next_page or url_for("dashboard"))
            flash("Invalid username or password.", "danger")
        return render_template("login.html", form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("You've been logged out.", "info")
        return redirect(url_for("login"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        modules = Module.query.order_by(Module.order).all()
        progress_map = {p.module_id: p for p in current_user.progress}
        unlocked_up_to = current_user.highest_unlocked_module()
        completed_count = sum(1 for p in current_user.progress if p.completed)
        if completed_count == len(modules):
            return redirect(url_for("completion"))
        return render_template(
            "dashboard.html",
            modules=modules,
            progress_map=progress_map,
            unlocked_up_to=unlocked_up_to,
            completed_count=completed_count,
            total_modules=len(modules),
        )

    @app.route("/module/<int:module_id>")
    @login_required
    def module_theory(module_id):
        module = Module.query.get_or_404(module_id)
        if not module_unlocked(current_user, module.order):
            flash("Complete the previous module first to unlock this one.", "warning")
            return redirect(url_for("dashboard"))
        prog = get_or_create_progress(current_user, module.id)
        prog.theory_viewed = True
        db.session.commit()
        return render_template("lesson.html", module=module, progress=prog)

    @app.route("/module/<int:module_id>/quiz", methods=["GET", "POST"])
    @login_required
    def quiz(module_id):
        module = Module.query.get_or_404(module_id)
        if not module_unlocked(current_user, module.order):
            flash("Complete the previous module first to unlock this one.", "warning")
            return redirect(url_for("dashboard"))
        questions = QuizQuestion.query.filter_by(module_id=module.id).all()

        if request.method == "POST":
            score = 0
            for q in questions:
                submitted = request.form.get(f"q{q.id}")
                if submitted == q.correct_option:
                    score += 1
            total = len(questions)
            prog = get_or_create_progress(current_user, module.id)
            prog.quiz_score = score
            prog.quiz_total = total
            prog.quiz_passed = score >= max(1, round(total * 0.6))
            db.session.commit()
            return render_template("quiz_result.html", module=module, score=score, total=total, prog=prog)

        return render_template("quiz.html", module=module, questions=questions)

    @app.route("/module/<int:module_id>/game")
    @login_required
    def game(module_id):
        module = Module.query.get_or_404(module_id)
        if not module_unlocked(current_user, module.order):
            flash("Complete the previous module first to unlock this one.", "warning")
            return redirect(url_for("dashboard"))
        prog = get_or_create_progress(current_user, module.id)
        if not prog.quiz_passed:
            flash("Pass the quiz first to unlock the memory challenge.", "warning")
            return redirect(url_for("quiz", module_id=module.id))
        riddles = Riddle.query.filter_by(module_id=module.id).all()
        return render_template("game.html", module=module, riddles=riddles)

    @app.route("/module/<int:module_id>/complete", methods=["POST"])
    @login_required
    def complete_module(module_id):
        module = Module.query.get_or_404(module_id)
        prog = get_or_create_progress(current_user, module.id)
        if not prog.quiz_passed:
            return jsonify({"ok": False, "error": "Quiz not passed yet."}), 400
        prog.game_completed = True
        prog.completed = True
        prog.completed_at = datetime.utcnow()
        db.session.commit()
        return jsonify({"ok": True, "next_unlocked": current_user.highest_unlocked_module()})

    @app.route("/profile", methods=["GET", "POST"])
    @login_required
    def profile():
        username_form = UpdateUsernameForm(prefix="uname")
        password_form = UpdatePasswordForm(prefix="pwd")
        photo_form = UpdatePhotoForm(prefix="photo")

        if request.method == "POST":
            form_type = request.form.get("form_type")

            if form_type == "uname-submit" and username_form.validate_on_submit():
                existing = User.query.filter_by(username=username_form.username.data.strip()).first()
                if existing and existing.id != current_user.id:
                    flash("That username is already taken.", "danger")
                else:
                    current_user.username = username_form.username.data.strip()
                    db.session.commit()
                    flash("Username updated.", "success")
                return redirect(url_for("profile"))

            if form_type == "pwd-submit" and password_form.validate_on_submit():
                if not current_user.check_password(password_form.current_password.data):
                    flash("Current password is incorrect.", "danger")
                else:
                    current_user.set_password(password_form.new_password.data)
                    db.session.commit()
                    flash("Password updated.", "success")
                return redirect(url_for("profile"))

            if form_type == "photo-submit":
                file = request.files.get("photo-photo")
                if file and file.filename:
                    if allowed_file(file.filename):
                        ext = file.filename.rsplit(".", 1)[1].lower()
                        filename = secure_filename(f"{current_user.id}_{uuid.uuid4().hex}.{ext}")
                        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                        file.save(filepath)
                        current_user.profile_pic = filename
                        db.session.commit()
                        flash("Profile photo updated.", "success")
                    else:
                        flash("Invalid file type. Use png, jpg, jpeg, or gif.", "danger")
                return redirect(url_for("profile"))

        return render_template(
            "profile.html",
            username_form=username_form,
            password_form=password_form,
            photo_form=photo_form,
        )

    @app.route("/setup-security", methods=["GET", "POST"])
    @login_required
    def setup_security():
        form = SecurityQuestionForm()
        if form.validate_on_submit():
            current_user.security_question = "What is your pet's name?"
            current_user.security_answer = form.security_answer.data.strip().lower()
            db.session.commit()
            flash("Security question saved successfully.", "success")
            return redirect(url_for("profile"))
        return render_template("setup_security.html", form=form)

    @app.route("/forgot-password", methods=["GET", "POST"])
    def forgot_password():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))
        form = ForgotPasswordForm()
        if form.validate_on_submit():
            user = User.query.filter_by(
                username=form.username.data.strip(),
                email=form.email.data.strip().lower()
            ).first()
            if user and user.security_answer:
                if user.security_answer == form.security_answer.data.strip().lower():
                    session["reset_user_id"] = user.id
                    flash("Identity verified. Please set your new password.", "success")
                    return redirect(url_for("reset_password"))
                else:
                    flash("Security answer is incorrect.", "danger")
            else:
                flash("No account found or security question not set.", "danger")
        return render_template("forgot_password.html", form=form)

    @app.route("/reset-password", methods=["GET", "POST"])
    def reset_password():
        user_id = session.get("reset_user_id")
        if not user_id:
            flash("Invalid or expired reset session. Please try again.", "danger")
            return redirect(url_for("forgot_password"))
        form = ResetPasswordForm()
        if form.validate_on_submit():
            user = db.session.get(User, user_id)
            if user:
                user.set_password(form.new_password.data)
                db.session.commit()
                session.pop("reset_user_id", None)
                flash("Password reset successfully. You can now log in.", "success")
                return redirect(url_for("login"))
        return render_template("reset_password.html", form=form)

    @app.route("/completion")
    @login_required
    def completion():
        completed_count = sum(1 for p in current_user.progress if p.completed)
        if completed_count < 7:
            return redirect(url_for("dashboard"))
        return render_template("completion.html")

    @app.route("/reset-progress", methods=["GET", "POST"])
    @login_required
    def reset_progress():
        Progress.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        flash("Progress reset! Start fresh from Module 1.", "success")
        return redirect(url_for("dashboard"))

    @app.cli.command("seed-db")
    def seed_db():
        db.create_all()
        if Module.query.first():
            print("Database already seeded. Skipping.")
            return
        for m in MODULES:
            module = Module(
                order=m["order"], title=m["title"], slug=m["slug"],
                summary=m["summary"], theory_html=m["theory_html"], icon=m["icon"],
            )
            db.session.add(module)
            db.session.flush()
            for q in m["quiz"]:
                db.session.add(QuizQuestion(
                    module_id=module.id, question=q["q"],
                    option_a=q["a"], option_b=q["b"], option_c=q["c"], option_d=q["d"],
                    correct_option=q["correct"],
                ))
            for term, clue in m["riddles"]:
                db.session.add(Riddle(module_id=module.id, term=term, clue=clue))
        db.session.commit()
        print(f"Seeded {len(MODULES)} modules.")

    return app


app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False, use_reloader=False)
