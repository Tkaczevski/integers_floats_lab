from unittest import TestCase
from integers_and_floats import integer_division, float_integer_multiplication, inputs_are_strings


class Test(TestCase):
    def test_integer_division(self):
        self.assertEqual(integer_division(), type(1.0))

    def test_float_integer_multiplication(self):
        self.assertEqual(float_integer_multiplication(), type(1.0))

    def test_inputs_are_strings(self):
        self.assertEqual(inputs_are_strings(), type(7 / 2.2))