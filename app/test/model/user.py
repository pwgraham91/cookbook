#!flask/bin/python
import unittest

from app.models import User
from app.test.base import BaseTestCase


class UserTestCase(BaseTestCase):
    def setUp(self) -> None:
        self.setUpDB()

    def tearDown(self) -> None:
        self.tearDownDB()

    def test_name_email(self):
        name = 'john'
        email = 'john@example.com'
        username = 'john123'
        u = self.get_test_user(name, email, username)
        self.session.add(u)
        john: User = self.session.query(User).one()
        self.assertEqual(john.name, name)
        self.assertEqual(john.email, email)
        self.assertEqual(john.username, username)


if __name__ == '__main__':
    unittest.main()
