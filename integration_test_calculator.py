import unittest
import tkinter as tk
from ScientificCal import SimpleCalculator, GUI, ScientificCalculator
# Mock event class to simulate button clicks
class MockEvent:
    def __init__(self, widget):
        self.widget = widget

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.simple_calculator = SimpleCalculator(self.root)
        self.gui = GUI(self.root)
        self.scientific_calculator = ScientificCalculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_simple_calculator_integration(self):
        # Simulate input and button click in simple calculator
        self.gui.screen_var.set('3+5*2')
        mock_event = MockEvent(tk.Button(self.root, text="="))
        self.gui.click(mock_event)
        result = self.gui.screen_var.get()
        self.assertEqual(result, '13')
        print("Simple calculator integration test passed")

    def test_scientific_calculator_integration(self):
        # Simulate input and button click in scientific calculator
        self.scientific_calculator.screen_var.set('sin(math.pi/2)')
        mock_event = MockEvent(tk.Button(self.root, text="="))
        self.scientific_calculator.click(mock_event)
        result = self.scientific_calculator.screen_var.get()
        self.assertEqual(result, '1.0')
        print("Scientific calculator integration test passed")

    def test_edge_case_division_by_zero(self):
        # Handle division by zero
        self.gui.screen_var.set('10/0')
        mock_event = MockEvent(tk.Button(self.root, text="="))
        self.gui.click(mock_event)
        result = self.gui.screen_var.get()
        self.assertEqual(result, 'Error')
        print("Division by zero edge case test passed")

    def test_invalid_input(self):
        # Handle invalid input
        self.gui.screen_var.set('3+')
        mock_event = MockEvent(tk.Button(self.root, text="="))
        self.gui.click(mock_event)
        result = self.gui.screen_var.get()
        self.assertEqual(result, 'Error')
        print("Invalid input test passed")

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestIntegration))
