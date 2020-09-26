import unittest
import katas
import math


class TestKatas(unittest.TestCase):

    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(katas.multiply(1, 5), 5)
        self.assertEqual(katas.multiply(-1, 1), -1)
        self.assertEqual(katas.multiply(1, -1), -1)
        self.assertEqual(katas.multiply(-1, -1), 1)

    def test_power(self):
        self.assertEqual(katas.power(1, 5), 1 ** 5)
        self.assertEqual(katas.power(-1, 3), -1 ** 3)
        self.assertEqual(katas.power(62, 0), 1)

    def test_factorial(self):
        self.assertEqual(katas.factorial(2), math.factorial(2))

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9), 21)
        self.assertEqual(katas.fibonacci(0), -1)
        self.assertEqual(katas.fibonacci(13), 144)
        self.assertEqual(katas.fibonacci(8), 13)
        self.assertEqual(katas.fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
