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
        self.assertEqual("1, 2, Fizz, 4, Buzz", self.fb.run(1, 6))
        self.assertEqual("Fizz, 7, 8, Fizz, Buzz", self.fb.run(6, 11))
        self.assertEqual("11, Fizz, 13, 14, FizzBuzz", self.fb.run(11, 16))
        self.assertEqual("FizzBuzz, 31, 32, Fizz, 34, Buzz",
                         self.fb.run(30, 36))


if __name__ == "__main__":
    unittest.main()
