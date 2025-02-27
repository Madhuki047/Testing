import unittest
import tkinter as tk
import numpy as np
from SciCalGraph import ScientificCal

class TestScientificCal(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.sci_cal = ScientificCal(self.root)
        self.sci_cal.sci_cal()  # Initialize the scientific calculator window to set up attributes

    def tearDown(self):
        self.root.destroy()

    def test_sin_function(self):
        x = np.deg2rad(np.linspace(-360, 360, 1000))
        expected_y = np.sin(x)
        self.sci_cal.selected_option.set('Sin')
        self.sci_cal.unit.set('Degrees')
        self.sci_cal.x_min_entry.delete(0, tk.END)
        self.sci_cal.x_min_entry.insert(0, "-360")
        self.sci_cal.x_max_entry.delete(0, tk.END)
        self.sci_cal.x_max_entry.insert(0, "360")
        self.sci_cal.plot_graph()
        np.testing.assert_array_almost_equal(self.sci_cal.y_data, expected_y)

    def test_cos_function(self):
        x = np.deg2rad(np.linspace(-360, 360, 1000))
        expected_y = np.cos(x)
        self.sci_cal.selected_option.set('Cos')
        self.sci_cal.unit.set('Degrees')
        self.sci_cal.x_min_entry.delete(0, tk.END)
        self.sci_cal.x_min_entry.insert(0, "-360")
        self.sci_cal.x_max_entry.delete(0, tk.END)
        self.sci_cal.x_max_entry.insert(0, "360")
        self.sci_cal.plot_graph()
        np.testing.assert_array_almost_equal(self.sci_cal.y_data, expected_y)

if __name__ == "__main__":
    unittest.main()