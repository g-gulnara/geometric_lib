import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_negative_area(self):
        res = area(-4)
        self.assertEqual(res, 16)  

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_negative_perimeter(self):
        res = perimeter(-4)
        self.assertEqual(res, -16)  # Периметр может быть отрицательным, если a отрицательно

if __name__ == '__main__':
    unittest.main()
