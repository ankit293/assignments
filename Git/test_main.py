import unittest
import main

class TestMain(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(main.fizzbuzz(2), [1, 2])
        self.assertEqual(main.fizzbuzz(10), [1, 2, "FIZZ", 4, "BUZZ", "FIZZ", 7, 8, "FIZZ", "BUZZ"])
        self.assertEqual(main.fizzbuzz(20), [1, 2, "FIZZ", 4, "BUZZ", "FIZZ", 7, 8, "FIZZ", "BUZZ", 11, "FIZZ", 13, 14 , "FIZZBUZZ", 16, 17, "FIZZ", 19, "BUZZ"])
        with self.assertRaises(ValueError):
            main.fizzbuzz(-1)

    def test_fibonacci(self):
        self.assertEqual(main.fibonacci(0), [0])
        self.assertEqual(main.fibonacci(1), [0, 1])
        self.assertEqual(main.fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        with self.assertRaises(ValueError):
            main.fibonacci(-1)
        
    def test_word_frequency(self):
        self.assertEqual(main.word_frequency("quick"), {"quick": 1})
        self.assertEqual(main.word_frequency("quick fox lazy dog quick donkey fire fox"), {"quick": 2, "fox": 2, "lazy": 1, "dog": 1, "donkey": 1, "fire": 1})
        with self.assertRaises(ValueError):
            main.word_frequency(" ")
        with self.assertRaises(ValueError):
            main.word_frequency("")


if __name__ == '__main__':
    unittest.main()