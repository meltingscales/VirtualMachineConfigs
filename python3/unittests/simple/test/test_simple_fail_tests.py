from unittest import TestCase


class FailTest(TestCase):
    def testFailure(self):
        self.assertTrue(False)