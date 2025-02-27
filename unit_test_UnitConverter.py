import unittest
from UnitConverter import UnitConverter

class TestUnitConverter(unittest.TestCase):

    def test_length_conversion(self):
        converter = UnitConverter(None)
        self.assertEqual(converter.perform_conversion(1000, "meter", "kilometer"), 1)
        self.assertEqual(converter.perform_conversion(1, "kilometer", "meter"), 1000)

    def test_weight_conversion(self):
        converter = UnitConverter(None)
        self.assertEqual(converter.perform_conversion(1000, "gram", "kilogram"), 1)
        self.assertEqual(converter.perform_conversion(1, "kilogram", "gram"), 1000)

    def test_temperature_conversion(self):
        converter = UnitConverter(None)
        self.assertEqual(converter.perform_conversion(0, "celsius", "fahrenheit"), 32)
        self.assertEqual(converter.perform_conversion(32, "fahrenheit", "celsius"), 0)

    def test_angle_conversion(self):
        converter = UnitConverter(None)
        self.assertAlmostEqual(converter.perform_conversion(180, "degree", "radian"), 3.141592653589793)
        self.assertAlmostEqual(converter.perform_conversion(3.141592653589793, "radian", "degree"), 180)

if __name__ == "__main__":
    unittest.main()