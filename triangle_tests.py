import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_triangle_area(self):
        res = area(6, 8)
        self.assertEqual(res, 24)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_equilateral_perimeter(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_scalene_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_negative_values_area(self):
        res = area(-10, 5)
        self.assertEqual(res, -25) 

    def test_negative_values_perimeter(self):
        res = perimeter(-3, 4, 5)
        self.assertEqual(res, 6)

if __name__ == '__main__':
    unittest.main()
