import unittest

from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    """FizzBuzz test class"""

    def test_fizzbuzz(self):
        """Test the FizzBuzz rules"""
        self.assertEqual("", FizzBuzz().run())


if __name__ == "__main__":
    unittest.main()
