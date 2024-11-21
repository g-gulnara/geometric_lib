import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483, places=5)

    def test_negative_area(self):
        res = area(-4)
        self.assertAlmostEqual(res, 50.26548245743669, places=5)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, places=5)

    def test_negative_perimeter(self):
        res = perimeter(-4)
        self.assertAlmostEqual(res, -25.1327412287191, places=5)
        
if __name__ == '__main__':
    unittest.main()
