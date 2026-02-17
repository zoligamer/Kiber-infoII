import unittest
from isprime import is_prime
class IsPrimeCase(unittest.TestCase):
    def test_is_prime_if_called_with_string(self):
        self.assertIsNone(is_prime("asd"))

if __name__ == "__main__":
    unittest.main()