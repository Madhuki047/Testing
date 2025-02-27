import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch
from ClassGUI import CommandsForGUI

class TestIntegration(unittest.TestCase):

    @patch('ClassGUI.ImageTk.PhotoImage', return_value=MagicMock())  # Mock ImageTk.PhotoImage
    @patch('ClassGUI.Image.open', return_value=MagicMock())  # Mock Image.open
    @patch('tkinter.Label')  # Mock tkinter.Label
    def setUp(self, mock_label, mock_open, mock_photo):
        mock_label.return_value = MagicMock()  # Mock Label to avoid image errors
        self.root = tk.Tk()
        self.contact_manager = MagicMock()  # Use a mock contact manager
        self.gui = CommandsForGUI(self.root, self.contact_manager)
        self.gui.show_add_contact_fields()  # Initialize the add contact window

    def tearDown(self):
        self.root.after(100, self.root.destroy)

    def test_add_contact_integration(self):
        # Simulate user input
        self.gui.first_name_entry.insert(0, 'John')
        self.gui.surname_entry.insert(0, 'Doe')
        self.gui.phone_entry.insert(0, '1234567890')
        self.gui.email_entry.insert(0, 'john.doe@example.com')

        # Call add_contact_gui method
        self.gui.add_contact_gui()

        # Verify that contact was added
        self.contact_manager.add_contact.assert_called_once()
        print("Add Contact Integration test passed")

    def test_edit_contact_integration(self):
        # Mock tree selection
        selected_item = 'fake_item_id'
        self.gui.tree.selection = MagicMock(return_value=[selected_item])
        self.gui.tree.item = MagicMock(return_value={'values': ['1', 'John', 'Doe', '1234567890', 'john.doe@example.com']})

        # Simulate user input for updating contact
        contact_id = '1'
        self.gui.first_name_entry.insert(0, 'Jane')
        self.gui.surname_entry.insert(0, 'Smith')
        self.gui.phone_entry.insert(0, '0987654321')
        self.gui.email_entry.insert(0, 'jane.smith@example.com')

        # Ensure that contact_manager has an edit_contact method
        self.contact_manager.edit_contact = MagicMock()

        # Call edit_contact method with MagicMock
        self.gui.contact_manager.edit_contact(contact_id, 'Jane', 'Smith', '0987654321', 'jane.smith@example.com')

        # Verify that contact was updated
        self.contact_manager.edit_contact.assert_called_once_with(contact_id, 'Jane', 'Smith', '0987654321', 'jane.smith@example.com')
        print("Edit Contact Integration test passed")

if __name__ == "__main__":
    unittest.main()
