import unittest
import math
from rectangle import *
from square import *
from circle import *
from triangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(rectangle_area(10, 0), 0)
        self.assertEqual(rectangle_area(0, 10), 0)

    def test_zero_sum(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_area_int_int(self):
        self.assertEqual(rectangle_area(5, 9), 45)
        self.assertEqual(rectangle_area(12, 7), 84)
        self.assertEqual(rectangle_area(1, 334), 334)

    def test_area_int_float(self):
        self.assertEqual(rectangle_area(5, 9.2), 46)
        self.assertEqual(rectangle_area(12, 7.31), 12 * 7.31)
        self.assertEqual(rectangle_area(1.001, 334), 1.001 * 334)

    def test_area_float_float(self):
        self.assertEqual(rectangle_area(5.3, 9.2), 5.3 * 9.2)
        self.assertEqual(rectangle_area(12.01, 7.3), 12.01 * 7.3)
        self.assertEqual(rectangle_area(1.01, 334.09), 1.01 * 334.09)

    def test_perimeter_int_int(self):
        self.assertEqual(rectangle_perimeter(5, 6), 22)
        self.assertEqual(rectangle_perimeter(12, 8), 40)
        self.assertEqual(rectangle_perimeter(1, 8), 18)

    def test_perimeter_int_float(self):
        self.assertEqual(rectangle_perimeter(5, 6.2), (5 + 6.2) * 2)
        self.assertEqual(rectangle_perimeter(12, 8.88), (12 + 8.88) * 2)
        self.assertEqual(rectangle_perimeter(1, 8.023), 18.046)

    def test_area_big_data(self):
        self.assertEqual(rectangle_area(51345670, 1269456), 51345670 * 1269456)

    def test_perimeter_big_data(self):
        self.assertEqual(rectangle_perimeter(1234567, 7654321), (1234567 + 7654321) * 2)


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_perimeter(0), 0)

    def test_zero_sum(self):
        self.assertEqual(square_perimeter(0), 0)


    def test_area_int(self):
        self.assertEqual(square_area(9), 81)
        self.assertEqual(square_area(12), 144)
        self.assertEqual(square_area(1), 1)

    def test_area_float(self):
        self.assertEqual(square_area(9.2), 9.2 * 9.2)
        self.assertEqual(square_area(7.31), 7.31 * 7.31)
        self.assertEqual(square_area(1.001), 1.001 * 1.001)

    def test_perimeter_int(self):
        self.assertEqual(square_perimeter(6), 24)
        self.assertEqual(square_perimeter(12), 48)
        self.assertEqual(square_perimeter(1),4)

    def test_perimeter_float(self):
        self.assertEqual(square_perimeter(6.2), 6.2 * 4)
        self.assertEqual(square_perimeter(8.88), 8.88 * 4)
        self.assertEqual(square_perimeter(8.023), 8.023 * 4)

    def test_area_big_data(self):
        self.assertEqual(square_area(51345670), 51345670 * 51345670)

    def test_perimeter_big_data(self):
        self.assertEqual(square_perimeter(7654321), 7654321 * 4)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(triangle_area(0, 10), 0)
        self.assertEqual(triangle_area(10, 0), 0)

    def test_zero_sum(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)

    def test_area_int_int(self):
        self.assertEqual(triangle_area(5, 9), 45 / 2)
        self.assertEqual(triangle_area(12, 7), 84 / 2)
        self.assertEqual(triangle_area(1, 334), 334 / 2)

    def test_area_int_float(self):
        self.assertEqual(triangle_area(5, 9.2), 46 / 2)
        self.assertEqual(triangle_area(12, 7.31), 12 * 7.31 / 2)
        self.assertEqual(triangle_area(1.001, 334), 1.001 * 334 / 2)

    def test_area_float_float(self):
        self.assertEqual(triangle_area(5.3, 9.2), 5.3 * 9.2 / 2)
        self.assertEqual(triangle_area(12.01, 7.3), 12.01 * 7.3 / 2)
        self.assertEqual(triangle_area(1.01, 334.09), 1.01 * 334.09 / 2)

    def test_perimeter_int_int_int(self):
        self.assertEqual(triangle_perimeter(5, 6, 7), 18)
        self.assertEqual(triangle_perimeter(12, 9, 20), 41)
        self.assertEqual(triangle_perimeter(5, 8, 4), 17)

    def test_perimeter_int_float_int(self):
        self.assertEqual(triangle_perimeter(5, 6.2, 1), (5 + 6.2 + 1))
        self.assertEqual(triangle_perimeter(12, 8.88, 10), (12 + 8.88 + 10))
        self.assertEqual(triangle_perimeter(1, 8.023, 100), 109.023)

    def test_perimeter_float_float_float(self):
        self.assertEqual(triangle_perimeter(5.1, 6.2, 1.1), (5.1 + 6.2 + 1.1))
        self.assertEqual(triangle_perimeter(12.2, 8.88, 10.2), (12.2 + 8.88 + 10.2))
        self.assertEqual(triangle_perimeter(1.3, 8.23, 100.3), 109.83)

    def test_area_big_data(self):
        self.assertEqual(triangle_area(51345670, 1269456), 51345670 * 1269456 / 2)

    def test_perimeter_big_data(self):
        self.assertEqual(triangle_perimeter(1234567, 7654321, 100000), (1234567 + 7654321 + 100000))

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_perimeter(0), 0)

    def test_zero_sum(self):
        self.assertEqual(circle_perimeter(0), 0)


    def test_area_int(self):
        self.assertEqual(circle_area(9), math.pi * 9 * 9)
        self.assertEqual(circle_area(12), math.pi * 12 * 12)
        self.assertEqual(circle_area(1), math.pi)

    def test_area_float(self):
        self.assertEqual(circle_area(9.2), math.pi * 9.2 * 9.2)
        self.assertEqual(circle_area(7.31), math.pi * 7.31 * 7.31)
        self.assertEqual(circle_area(1.001), math.pi * 1.001 * 1.001)

    def test_perimeter_int(self):
        self.assertEqual(circle_perimeter(6), 12 * math.pi)
        self.assertEqual(circle_perimeter(12), 24 * math.pi)
        self.assertEqual(circle_perimeter(1), 2 * math.pi)

    def test_perimeter_float(self):
        self.assertEqual(circle_perimeter(6.2), 6.2 * 2 * math.pi)
        self.assertEqual(circle_perimeter(8.88), 8.88 * 2 * math.pi)
        self.assertEqual(circle_perimeter(8.023), 8.023 * 2 * math.pi)

    def test_area_big_data(self):
        self.assertEqual(circle_area(51345670), math.pi * 51345670 * 51345670)

    def test_perimeter_big_data(self):
        self.assertEqual(circle_perimeter(7654321), 7654321 * 2 * math.pi)