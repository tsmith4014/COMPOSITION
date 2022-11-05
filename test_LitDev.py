import unittest

from litD import LitDev


class TestLitDev(unittest.TestCase):

    def test_initializes_correctly(self):
        ld = LitDev("hi")
        expected = "hi"
        actual = ld.text
        self.assertEqual(expected, actual)

    def test_palindrome_logic(self):
        actual = LitDev._test_word_is_palindrome("racecar")
        expected = True
        self.assertEqual(actual, expected)

    def test_has_palindrome_works_false(self):
        ld = LitDev("hi")
        actual = ld.has_palindrome()
        self.assertFalse(actual)
        self.assertIs(actual, False)

    def test_has_palindrome_works_true(self):
        ld = LitDev("racecar")
        actual = ld.has_palindrome()
        self.assertTrue(actual)

    def test_same_first_last(self):
        ld = LitDev("racecar is a racecar")
        actual = ld.same_first_and_last()
        self.assertTrue(actual)


if __name__ == "__main__":
    unittest.main()
