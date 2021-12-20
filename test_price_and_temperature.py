from unittest import TestCase
from price_and_temperature import unit_price, celsius_to_fahrenheit


class Test(TestCase):
    def test_unit_price(self):
        self.assertEqual(unit_price(), f"This product is ¥5.0/kg")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(), f"8°C is 46.4°F")
