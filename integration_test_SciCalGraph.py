import unittest
import tkinter as tk
import numpy as np
from SciCalGraph import ScientificCal

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.sci_cal = ScientificCal(self.root)
        self.sci_cal.sci_cal()  # Initialize the scientific calculator window to set up attributes

    def tearDown(self):
        self.root.after(100, self.root.destroy)

    def test_gui_initialization(self):
        # Test if the GUI elements are initialized correctly
        self.assertIn('toplevel', self.sci_cal.scientific_window.winfo_name(), "Window name does not contain 'toplevel'")
        self.assertEqual(self.sci_cal.scientific_window.title(), 'Trigonometry Graphs', "Window title is not 'Trigonometry Graphs'")
        self.assertEqual(self.sci_cal.scientific_window['bg'], 'Lavender', "Window background is not 'Lavender'")
        print("GUI Initialization test passed")

    def test_plot_graph_integration(self):
        # Test if the GUI updates the plot correctly
        self.sci_cal.selected_option.set('Sin')
        self.sci_cal.unit.set('Degrees')
        self.sci_cal.x_min_entry.delete(0, tk.END)
        self.sci_cal.x_min_entry.insert(0, "-360")
        self.sci_cal.x_max_entry.delete(0, tk.END)
        self.sci_cal.x_max_entry.insert(0, "360")
        self.sci_cal.y_min_entry.delete(0, tk.END)
        self.sci_cal.y_min_entry.insert(0, "-1")
        self.sci_cal.y_max_entry.delete(0, tk.END)
        self.sci_cal.y_max_entry.insert(0, "1")
        self.sci_cal.plot_graph()
        expected_y = np.sin(np.deg2rad(self.sci_cal.x_data))
        np.testing.assert_array_almost_equal(self.sci_cal.y_data, expected_y)
        print("Plot Graph test passed")

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestIntegration))