import unittest
from isprime import is_prime
class IsPrimeCase(unittest.TestCase):
    def test_is_prime_if_called_with_string(self): ## string eseten ellenorzes
        self.assertIsNone(is_prime("asd"))



## negativ szam eseten ellenorzes
    def test_neg_num(self):
        self.assertFalse(is_prime(-1), msg='false must be the negative number operation')

    def test_isprime_calledwith_prime(self):
        primetest_vectors = [3,5,7,11,13,23,6899]
        for prime in primetest_vectors:
            self.assertTrue(is_prime(prime), msg=f'{prime} is prime but isprime returned not true')

    def testIsprimeCalledWithNOTPrime(self):
        notprime = [4,6,8,9,10,12,14,15,16,18,20]
        for np in notprime:
            self.assertFalse(is_prime(np), msg='prime but return with false')




        
if __name__ == "__main__":
    unittest.main()