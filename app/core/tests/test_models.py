from django.test import TestCase
from django.contrib.auth import get_user_model
from app.calc import add, subtract


class ModelTests(TestCase):

    def test_add_number(self):
        self.assertEqual(add(2, 5), 7)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(10, 5), 5)
