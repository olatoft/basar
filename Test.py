import unittest
import validation


class TestForm(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(validation.is_int('3'), True)
        self.assertEqual(validation.is_int('2.5'), False)
        self.assertEqual(validation.is_int('-3'), True)
        self.assertEqual(validation.is_int('0'), True)
        self.assertEqual(validation.is_int('tre'), False)
        self.assertEqual(validation.is_int(''), False)

    def test_is_positive(self):
        self.assertEqual(validation.is_positive(3), True)
        self.assertEqual(validation.is_positive(-3), False)
        self.assertEqual(validation.is_positive(0), False)

    def test_is_bigger(self):
        self.assertEqual(validation.is_bigger(2, 3), True)
        self.assertEqual(validation.is_bigger(3, 2), False)
        self.assertEqual(validation.is_bigger(3, 3), False)

if __name__ == '__main__':
    unittest.main()
