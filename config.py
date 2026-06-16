import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Secret key used for session signing / CSRF tokens. Always override via env var in production.
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-me-in-production")

    # --- Database ---
    # MySQL connection. Falls back to SQLite for quick local testing if MYSQL vars aren't set.
    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_DB = os.environ.get("MYSQL_DB", "cyberverse")

    if MYSQL_USER and MYSQL_PASSWORD:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
        )
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'cyberverse.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Session / cookie security ---
    SESSION_COOKIE_HTTPONLY = True          # JS cannot read the session cookie (mitigates XSS theft)
    SESSION_COOKIE_SAMESITE = "Lax"         # mitigates basic CSRF via cross-site requests
    SESSION_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"  # HTTPS-only in prod
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 2  # 2 hour session timeout

    # --- File uploads ---
    UPLOAD_FOLDER = os.path.join(basedir, "static", "uploads", "profile_pics")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # 2 MB max upload
