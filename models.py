from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String(255), default="default.png")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Streak tracking
    current_streak = db.Column(db.Integer, default=0)
    longest_streak = db.Column(db.Integer, default=0)
    last_active_date = db.Column(db.Date, nullable=True)

    # Security questions
    security_question = db.Column(db.String(255), nullable=True)
    security_answer = db.Column(db.String(255), nullable=True)
    security_answer2 = db.Column(db.String(255), nullable=True)
    security_answer3 = db.Column(db.String(255), nullable=True)

    progress = db.relationship("Progress", backref="user", lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def highest_unlocked_module(self):
        completed_ids = sorted(p.module_id for p in self.progress if p.completed)
        next_id = 1
        for mid in completed_ids:
            if mid == next_id:
                next_id += 1
        return next_id

    def is_module_completed(self, module_id):
        return any(p.module_id == module_id and p.completed for p in self.progress)

    def update_streak(self):
        today = datetime.utcnow().date()
        if self.last_active_date == today:
            return
        if self.last_active_date is not None and (today - self.last_active_date).days == 1:
            self.current_streak += 1
        else:
            self.current_streak = 1
        self.longest_streak = max(self.longest_streak, self.current_streak)
        self.last_active_date = today


class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    summary = db.Column(db.String(255))
    theory_html = db.Column(db.Text)
    icon = db.Column(db.String(50), default="shield")

    questions = db.relationship("QuizQuestion", backref="module", lazy=True, cascade="all, delete-orphan")
    riddles = db.relationship("Riddle", backref="module", lazy=True, cascade="all, delete-orphan")


class QuizQuestion(db.Model):
    __tablename__ = "quiz_questions"

    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"), nullable=False)
    question = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_option = db.Column(db.String(1), nullable=False)


class Riddle(db.Model):
    __tablename__ = "riddles"

    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"), nullable=False)
    term = db.Column(db.String(120), nullable=False)
    clue = db.Column(db.String(255), nullable=False)


class Progress(db.Model):
    __tablename__ = "progress"
    __table_args__ = (db.UniqueConstraint("user_id", "module_id", name="uix_user_module"),)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey("modules.id"), nullable=False)

    theory_viewed = db.Column(db.Boolean, default=False)
    quiz_score = db.Column(db.Integer, default=0)
    quiz_total = db.Column(db.Integer, default=0)
    quiz_passed = db.Column(db.Boolean, default=False)
    game_completed = db.Column(db.Boolean, default=False)
    completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)
