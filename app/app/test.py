from django.test import TestCase
from app.calc import subtract


class CalcTests(TestCase):

    def test_subtract_number(self):
        self.assertEqual(subtract(12, 6), 6)
