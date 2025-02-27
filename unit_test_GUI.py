import unittest
import tkinter as tk
from unittest.mock import MagicMock
from ClassGUI import CommandsForGUI

class TestCommandsForGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.contact_manager = MagicMock()  # Use a mock contact manager
        self.gui = CommandsForGUI(self.root, self.contact_manager)
        self.gui.show_add_contact_fields()  # Initialize the add contact window

    def tearDown(self):
        self.root.destroy()

    def test_show_add_contact_fields(self):
        self.assertEqual(self.gui.add_contact_window.winfo_class(), 'Toplevel')
        self.assertEqual(self.gui.add_contact_window.title(), 'Add Contact')
        self.assertEqual(self.gui.add_contact_window['bg'], '#A8E6CF')

    def test_add_contact_gui(self):
        self.gui.first_name_entry.insert(0, 'John')
        self.gui.surname_entry.insert(0, 'Doe')
        self.gui.phone_entry.insert(0, '1234567890')
        self.gui.email_entry.insert(0, 'john.doe@example.com')
        self.gui.add_contact_gui()
        self.contact_manager.add_contact.assert_called_once()

if __name__ == "__main__":
    unittest.main()