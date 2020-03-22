import unittest
import uuid

from sqlalchemy.orm import Session

from app import app, db
from app.lib.user_lib import create_user
from app.models import User
from test_config import SQLALCHEMY_TEST_DATABASE_URI


class BaseTestCase(unittest.TestCase):
    session: Session

    def setUpDB(self) -> None:
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_TEST_DATABASE_URI
        self.app = app.test_client()
        db.create_all()
        self.session: Session = db.session

    @staticmethod
    def tearDownDB():
        db.session.remove()
        db.drop_all()

    @staticmethod
    def get_test_user(name=None, email=None, username=None, password='password') -> User:
        name = name or uuid.uuid4()
        username = username or uuid.uuid4()
        email = email or '{}@gmail.com'.format(uuid.uuid4())
        user = create_user({
            'name': name,
            'username': username,
            'email': email,
            'password': password
        })

        return user
