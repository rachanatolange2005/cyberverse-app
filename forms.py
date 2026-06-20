from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError, Regexp
)
from models import User


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[
        DataRequired(), Length(min=3, max=25),
        Regexp(r"^[A-Za-z0-9_]+$", message="Username can only contain letters, numbers, and underscores.")
    ])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[
        DataRequired(), Length(min=8, message="Password must be at least 8 characters."),
        Regexp(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$",
               message="Password must include an uppercase letter, a lowercase letter, and a number.")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo("password", message="Passwords must match.")
    ])
    submit = SubmitField("Create Account")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("That username is already taken.")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("An account with this email already exists.")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Log In")


class UpdateUsernameForm(FlaskForm):
    username = StringField("New Username", validators=[
        DataRequired(), Length(min=3, max=25),
        Regexp(r"^[A-Za-z0-9_]+$", message="Username can only contain letters, numbers, and underscores.")
    ])
    submit = SubmitField("Update Username")


class UpdatePasswordForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[
        DataRequired(), Length(min=8, message="Password must be at least 8 characters."),
        Regexp(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$",
               message="Password must include an uppercase letter, a lowercase letter, and a number.")
    ])
    confirm_new_password = PasswordField("Confirm New Password", validators=[
        DataRequired(), EqualTo("new_password", message="Passwords must match.")
    ])
    submit = SubmitField("Update Password")


class UpdatePhotoForm(FlaskForm):
    photo = FileField("Profile Photo", validators=[
        FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only (jpg, jpeg, png, gif).")
    ])
    submit = SubmitField("Update Photo")

class SecurityQuestionForm(FlaskForm):
    security_answer = StringField("What is your pet's name?", validators=[
        DataRequired(), Length(min=1, max=100)
    ])
    security_answer2 = StringField("What is your favourite childhood friend's name?", validators=[
        DataRequired(), Length(min=1, max=100)
    ])
    security_answer3 = StringField("What is your favourite movie?", validators=[
        DataRequired(), Length(min=1, max=100)
    ])
    submit = SubmitField("Set Security Answers")


class ForgotPasswordForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    security_answer = StringField("What is your pet's name?", validators=[DataRequired()])
    security_answer2 = StringField("What is your favourite childhood friend's name?", validators=[DataRequired()])
    security_answer3 = StringField("What is your favourite movie?", validators=[DataRequired()])
    submit = SubmitField("Verify Identity")


class ResetPasswordForm(FlaskForm):
    new_password = PasswordField("New Password", validators=[
        DataRequired(), Length(min=8),
        Regexp(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$",
               message="Password must include uppercase, lowercase and a number.")
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo("new_password", message="Passwords must match.")
    ])
    submit = SubmitField("Reset Password")
