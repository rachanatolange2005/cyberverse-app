import unittest
import os

# Force SQLite BEFORE importing anything else
os.environ["TESTING"] = "true"

from app import create_app
from models import db, User, Module, Progress


class CyberVerseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        self.app.config["WTF_CSRF_ENABLED"] = False
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()
        db.create_all()

        user = User(username="testuser", email="test@test.com")
        user.set_password("Test1234")
        db.session.add(user)

        module = Module(
            order=1,
            title="Phishing Awareness",
            slug="phishing-awareness",
            summary="Test summary",
            theory_html="<p>Test theory</p>",
            icon="fish"
        )
        db.session.add(module)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        print("PASS - Home page loads")

    def test_register_page_loads(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)
        print("PASS - Register page loads")

    def test_login_page_loads(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        print("PASS - Login page loads")

    def test_valid_registration(self):
        response = self.client.post("/register", data={
            "username": "newuser",
            "email": "newuser@test.com",
            "password": "NewPass1",
            "confirm_password": "NewPass1"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("PASS - Valid registration works")

    def test_duplicate_username_rejected(self):
        response = self.client.post("/register", data={
            "username": "testuser",
            "email": "another@test.com",
            "password": "Test1234",
            "confirm_password": "Test1234"
        }, follow_redirects=True)
        self.assertIn(b"already taken", response.data)
        print("PASS - Duplicate username rejected")

    def test_valid_login(self):
        response = self.client.post("/login", data={
            "username": "testuser",
            "password": "Test1234"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("PASS - Valid login works")

    def test_invalid_login(self):
        response = self.client.post("/login", data={
            "username": "testuser",
            "password": "wrongpassword"
        }, follow_redirects=True)
        self.assertIn(b"Invalid username or password", response.data)
        print("PASS - Invalid login rejected")

    def test_logout(self):
        self.client.post("/login", data={
            "username": "testuser",
            "password": "Test1234"
        })
        response = self.client.get("/logout", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print("PASS - Logout works")

    def test_dashboard_requires_login(self):
        response = self.client.get("/dashboard", follow_redirects=True)
        self.assertIn(b"Log In", response.data)
        print("PASS - Dashboard requires login")

    def test_profile_requires_login(self):
        response = self.client.get("/profile", follow_redirects=True)
        self.assertIn(b"Log In", response.data)
        print("PASS - Profile requires login")

    def test_module_requires_login(self):
        response = self.client.get("/module/1", follow_redirects=True)
        self.assertIn(b"Log In", response.data)
        print("PASS - Module requires login")

    def test_completion_requires_login(self):
        response = self.client.get("/completion", follow_redirects=True)
        self.assertIn(b"Log In", response.data)
        print("PASS - Completion page requires login")

    def test_password_is_hashed(self):
        user = User.query.filter_by(username="testuser").first()
        self.assertNotEqual(user.password_hash, "Test1234")
        self.assertTrue(user.check_password("Test1234"))
        print("PASS - Password is hashed correctly")

    def test_weak_password_rejected(self):
        response = self.client.post("/register", data={
            "username": "weakuser",
            "email": "weak@test.com",
            "password": "weak",
            "confirm_password": "weak"
        }, follow_redirects=True)
        self.assertNotIn(b"Account created", response.data)
        print("PASS - Weak password rejected")

    def test_password_mismatch_rejected(self):
        response = self.client.post("/register", data={
            "username": "mismatch",
            "email": "mismatch@test.com",
            "password": "Test1234",
            "confirm_password": "Test5678"
        }, follow_redirects=True)
        self.assertNotIn(b"Account created", response.data)
        print("PASS - Password mismatch rejected")

    def test_user_saved_in_database(self):
        user = User.query.filter_by(username="testuser").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "test@test.com")
        print("PASS - User saved in database")

    def test_module_saved_in_database(self):
        module = Module.query.filter_by(slug="phishing-awareness").first()
        self.assertIsNotNone(module)
        self.assertEqual(module.order, 1)
        print("PASS - Module saved in database")

    def test_progress_record_creation(self):
        user = User.query.filter_by(username="testuser").first()
        module = Module.query.first()
        progress = Progress(user_id=user.id, module_id=module.id, theory_viewed=True)
        db.session.add(progress)
        db.session.commit()
        saved = Progress.query.filter_by(user_id=user.id).first()
        self.assertIsNotNone(saved)
        self.assertTrue(saved.theory_viewed)
        print("PASS - Progress record created")

    def test_new_user_streak_is_zero(self):
        user = User.query.filter_by(username="testuser").first()
        self.assertEqual(user.current_streak, 0)
        print("PASS - New user streak starts at 0")

    def test_new_user_unlocks_only_module_one(self):
        user = User.query.filter_by(username="testuser").first()
        self.assertEqual(user.highest_unlocked_module(), 1)
        print("PASS - New user can only access module 1")

    def test_default_profile_pic(self):
        user = User.query.filter_by(username="testuser").first()
        self.assertEqual(user.profile_pic, "default.png")
        print("PASS - Default profile picture set correctly")


if __name__ == "__main__":
    unittest.main(verbosity=2)