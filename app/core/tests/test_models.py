from django.test import TestCase
from django.contrib.auth import get_user_model
from app.calc import add, subtract


class ModelTests(TestCase):

    def test_add_number(self):
        self.assertEqual(add(2, 5), 7)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_create_user_with_successful(self):
        email = 'test@urkrainedev.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
