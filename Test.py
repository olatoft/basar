import unittest
import validation
from flask import Flask, flash, request


class TestForm(unittest.TestCase):

    def test_is_bigger(self):
        self.assertEqual(validation.is_bigger(2, 3), True)
        self.assertEqual(validation.is_bigger(3, 2), False)
        self.assertEqual(validation.is_bigger(3, 3), False)

if __name__ == '__main__':
    unittest.main()
