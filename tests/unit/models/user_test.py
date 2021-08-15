from models.user.user import User
from unittest import TestCase


class UserTest(TestCase):
    def test_create_user(self):
        user = User('Test', 'Test@test.com', 'abcd', 0)

        self.assertEqual(user._name, 'Test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user._email, 'Test@test.com',
                         "The email of the user after creation does not equal the constructor argument.")
        self.assertEqual(user._password, 'abcd',
                         "The password of the user after creation does not equal the constructor argument.")
        self.assertEqual(user._blocked, 0,
                         "The blocked of the user after creation does not equal the constructor argument.")


