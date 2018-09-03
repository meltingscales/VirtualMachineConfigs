from django.test import TestCase
from .views import *


class CoolTestCase(TestCase):

    def test_this_will_fail(self):
        self.assertTrue(False)

    def test_sanity(self):
        self.assertEqual(a_function(), "beans")  # Can we import functions?

        self.assertEqual(True, True)  # Sanity check

        self.assertEqual(1 * 3, 3)  # Can we do math?

    def test_random_numbers(self):  # Test the random numbers function.

        for i in range(0, 50000):  # Do it 50,000 times!
            x = random_numbers_1_100()

            self.assertTrue((x >= 0) and (x <= 100))  # Make sure it's between 0,100.
