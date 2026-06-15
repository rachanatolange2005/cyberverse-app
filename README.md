# CyberVerse 🛡️
**Interactive Cybersecurity Learning Portal**

> ST5041CMD — The Internet and Web Technologies · Softwarica College of IT & E-Commerce / Coventry University

---

## Project Overview

CyberVerse is a Flask-based web application that teaches foundational cybersecurity through 7 interactive modules. Each module contains:

1. **Theory** — readable, structured lesson content
2. **Quiz** — 5 multiple-choice questions (60% pass mark required to advance)
3. **Memory Challenge** — a card-matching game that reinforces terminology

Users must complete each module (theory → quiz → game) before the next one unlocks. The app tracks daily login streaks and allows full profile management (username, password, profile photo).

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (Vanilla), Jinja2 |
| Backend | Python 3, Flask, Flask-Login, Flask-WTF |
| Database | MySQL (via SQLAlchemy ORM) / SQLite (dev fallback) |
| Auth | werkzeug password hashing (PBKDF2+SHA256), CSRF tokens |
| Version Control | Git + GitHub |

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- MySQL server running (or use the SQLite fallback for quick local testing)
- Git

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/cyberverse.git
cd cyberverse
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment
```bash
cp .env.example .env
# Edit .env and fill in your SECRET_KEY and MySQL credentials.
# Leave MYSQL_USER blank to use SQLite automatically.
```

### 4. Set up the database
```bash
# Create the MySQL database first (if using MySQL):
mysql -u root -p -e "CREATE DATABASE cyberverse CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Then seed it:
flask seed-db
```

### 5. Run the development server
```bash
python app.py
```
Visit [http://localhost:5000](http://localhost:5000)

---

## Project Structure

```
cyberverse/
├── app.py              # Flask app factory + all routes
├── models.py           # SQLAlchemy models (User, Module, QuizQuestion, Riddle, Progress)
├── forms.py            # WTForms (Register, Login, UpdateUsername, UpdatePassword, UpdatePhoto)
├── content.py          # Seed content for all 7 modules (theory, quiz, riddles)
├── config.py           # Centralised config (env vars, session settings, upload paths)
├── requirements.txt
├── .env.example
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   ├── img/default.svg
│   └── uploads/profile_pics/
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── lesson.html
    ├── quiz.html
    ├── quiz_result.html
    ├── game.html
    └── profile.html
```

---

## Security Measures

- **Password hashing** — werkzeug PBKDF2+SHA256 with random salt; never stored in plain text
- **CSRF protection** — Flask-WTF tokens on every form POST
- **Secure session cookies** — HttpOnly, SameSite=Lax; Secure flag enabled in production
- **Input validation** — WTForms server-side validation + regex constraints on usernames/passwords
- **Generic auth error messages** — "Invalid username or password" (never confirms which is wrong)
- **File upload validation** — extension whitelist + 2 MB size cap; filenames sanitised with `secure_filename`
- **Environment-based secrets** — `SECRET_KEY` and DB credentials read from `.env`, never hardcoded
- **SQL injection prevention** — all queries via SQLAlchemy ORM (parameterised)
- **Session timeout** — 2-hour idle expiry

---

## Video Demonstration

> Link: _[Add YouTube/Drive link here after recording]_

---

## Version Control

> GitHub Repository: _[Add your GitHub repo link here]_

Commit history follows conventional structure: `feat:`, `fix:`, `docs:`, `style:`.
