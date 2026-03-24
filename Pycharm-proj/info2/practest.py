import unittest
from niggap_ractice import RandomNumber, EvenNumber, FileNumbers
class RandomNumberTestCase(unittest.TestCase):
    def test_random_numbers(self):
        random_generator=RandomNumber()
        number = random_generator.get_random_number()
        self.assertIsInstance(number,float)
        count=5
        while count>0:
            number=next(random_generator)
            self.assertIsInstance(number,float)
            count-=1
        count=5
        for number in random_generator:
            if count==0:
                break
            self.assertIsInstance(number,float)
            count-=1


class EvenNumberTestCase(unittest.TestCase):
    def test_even_numbers_logic(self):
        # Az __init__ meghívása: példányosítunk egy objektumot 10-es maximummal
        # Itt a self.max = 10 és a self.actual = 0 lesz
        even_gen = EvenNumber(max=10)

        # Első hívás tesztelése (0 + 2 = 2.0)
        number = even_gen.get_number()
        self.assertEqual(2.0, number)
        self.assertIsInstance(number, float)

    def test_even_iteration_with_next(self):
        even_gen = EvenNumber(max=20)
        # A get_number() már lefutott az előző tesztben, itt egy új példányunk van
        # A next() belsőleg a get_number()-t hívja meg
        self.assertEqual(2.0, next(even_gen))
        self.assertEqual(4.0, next(even_gen))
        self.assertEqual(6.0, next(even_gen))

    def test_even_for_loop(self):
        # A for ciklus az __iter__ és __next__ metódusokat használja
        max_limit = 6
        even_gen = EvenNumber(max=max_limit)
        results = []

        for number in even_gen:
            results.append(number)

        # Elvárt eredmények: 2.0, 4.0, 6.0
        self.assertEqual([2.0, 4.0, 6.0], results)
class FileNumTestCase(unittest.TestCase):
    def test_file_num(self):
        file_num_generator=FileNumbers("data.dat")
        for number in file_num_generator:
            self.assertIsInstance(number,float)
if __name__ == '__main__':
    unittest.main()
