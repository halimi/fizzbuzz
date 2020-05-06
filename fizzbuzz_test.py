import unittest

from fizzbuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    """FizzBuzz test class"""

    def setUp(self):
        """Setup the test environment"""
        self.fb = FizzBuzz()

    def test_fizzbuzz(self):
        """Test the FizzBuzz rules"""
        self.assertEqual("", self.fb.run(1, 1))
        self.assertEqual("1", self.fb.run(1, 2))
        self.assertEqual("1, 2", self.fb.run(1, 3))
        self.assertEqual("1, 2, Fizz", self.fb.run(1, 4))


if __name__ == "__main__":
    unittest.main()
