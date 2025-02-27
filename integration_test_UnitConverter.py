import unittest
import tkinter as tk
from UnitConverter import UnitConverter

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.unit_converter = UnitConverter(self.root)
    def tearDown(self):
        self.root.destroy()
    def test_gui_initialization(self):
        # Test if the GUI elements are initialized correctly
        self.assertIn('toplevel', self.unit_converter.window.winfo_name(), "Window name does not contain 'toplevel'")
        self.assertEqual(self.unit_converter.window.title(), 'Unit Converter', "Window title is not 'Unit Converter'")
        self.assertEqual(self.unit_converter.window['bg'], 'Thistle', "Window background is not 'Thistle'")
        print("test_gui_initialization successful")

    def test_unit_conversion_integration(self):
        # Test if the GUI updates the result correctly
        self.unit_converter.entry_var.set('1')
        self.unit_converter.unit_from_var.set('meter')
        self.unit_converter.unit_to_var.set('kilometer')
        self.unit_converter.convert_units()
        self.assertEqual(self.unit_converter.result_var.get(), '0.001')
        print("test_unit_conversion_integration successful")

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestIntegration))