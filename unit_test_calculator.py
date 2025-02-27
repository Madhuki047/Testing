import unittest
import tkinter as tk
from unittest.mock import MagicMock
from ScientificCal import SimpleCalculator, GUI, ScientificCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.calculator = SimpleCalculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.assertEqual(self.calculator.root.title(), "Simple Calculator")
        self.assertEqual(self.calculator.root['bg'], "White")

    def test_menu_creation(self):
        menu = self.calculator.root.children['!menu']
        self.assertIsNotNone(menu)
        self.assertEqual(menu.index('end'), 3)

    def test_new_cal(self):
        self.calculator.new_cal()
        top_level_windows = [w for w in self.calculator.root.winfo_children() if isinstance(w, tk.Toplevel)]
        self.assertEqual(len(top_level_windows), 1)
        self.assertEqual(top_level_windows[0].title(), "Simple Calculator (New)")

    def test_help_button(self):
        self.calculator.help_button()
        top_level_windows = [w for w in self.calculator.root.winfo_children() if isinstance(w, tk.Toplevel)]
        self.assertEqual(len(top_level_windows), 1)
        self.assertEqual(top_level_windows[0].title(), "Help")

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.gui = GUI(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.assertIsInstance(self.gui.screen_var, tk.StringVar)

    def test_create_widgets(self):
        widgets = self.gui.root.winfo_children()
        self.assertGreater(len(widgets), 0)  # Ensure widgets are created

    def test_click(self):
        # Simulate button clicks and verify the behavior
        self.gui.screen_var.set("2+2")
        self.gui.click(self.mock_event('='))
        self.assertEqual(self.gui.screen_var.get(), "4")

    def mock_event(self, char):
        class MockEvent:
            def __init__(self, char):
                self.widget = self.Widget(char)
            
            class Widget:
                def __init__(self, char):
                    self.char = char
                
                def cget(self, attr):
                    return self.char
        return MockEvent(char)

class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.sci_calculator = ScientificCalculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_initialization(self):
        self.assertIsInstance(self.sci_calculator.screen_var, tk.StringVar)

    def test_create_widgets(self):
        widgets = self.sci_calculator.root.winfo_children()
        self.assertGreater(len(widgets), 0)  # Ensure widgets are created

    def test_click(self):
        # Simulate button clicks and verify the behavior
        self.sci_calculator.screen_var.set("sin(math.pi/2)")
        self.sci_calculator.click(self.mock_event('='))
        self.assertEqual(self.sci_calculator.screen_var.get(), "1.0")

    def mock_event(self, char):
        class MockEvent:
            def __init__(self, char):
                self.widget = self.Widget(char)
            
            class Widget:
                def __init__(self, char):
                    self.char = char
                
                def cget(self, attr):
                    return self.char
        return MockEvent(char)

if __name__ == "__main__":
    unittest.main()