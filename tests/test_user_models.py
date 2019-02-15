from unittest import TestCase

from app import create_app
from app.database import db
from app.auth import models


class UserModelTest(TestCase):

    user = models.User(
        id=1,
        first_name='Test',
        last_name='Tests',
        username='tests',
        email="test@email.com",
        _password=123456,
        created_on='Mon, 01 Oct 2018 17:36:42 GMT',
        updated_on='Mon, 01 Oct 2018 17:36:42 GMT',
    )

    def setUp(self):
        self.app = create_app(__name__, 'testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_table_name_should_return_correct_name(self):

        expected = 'tb_users'
        self.assertEqual(self.user.__tablename__, expected)

    def test_table_repr_should_return_correct_user(self):

        expected = 'User(first_name="Test", last_name="Tests", username="tests", email="test@email.com", _password=123456)'
        self.assertEqual(self.user.__repr__(), expected)

    def test_table_str_should_return_correct_user(self):

        expected = '(tests) - test@email.com'
        self.assertEqual(self.user.__str__(), expected)

    def test_table_as_dict_should_return_corret_user(self):

        expected = {
            "_password": 123456,
            "created_on": "Mon, 01 Oct 2018 17:36:42 GMT",
            "email": "test@email.com",
            "first_name": "Test",
            "id": 1,
            "last_name": "Tests",
            "username": "tests",
            "updated_on": "Mon, 01 Oct 2018 17:36:42 GMT",
        }

        self.assertEqual(self.user.as_dict(), expected)
