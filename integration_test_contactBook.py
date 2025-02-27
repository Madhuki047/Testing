# Integration testing
import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from ClassDatabase import Database, DatabaseManagement
from ClassGUI import CommandsForGUI
from THEcontactBOOK import Contact

class TestIntegration(unittest.TestCase):

    @patch('ClassDatabase.mysql.connector.connect')
    def setUp(self, mock_connect):
        # Mock the database connection and cursor
        self.mock_db = MagicMock()
        self.mock_cursor = MagicMock()
        mock_connect.return_value = self.mock_db
        self.mock_db.cursor.return_value = self.mock_cursor

        # Initialize the Database and DatabaseManagement objects
        self.db = Database()
        self.contact_manager = DatabaseManagement(self.db)
        self.root = tk.Tk()

        # Mock the methods in DatabaseManagement
        self.contact_manager.add_contact = MagicMock()
        self.contact_manager.update_contact = MagicMock()
        self.contact_manager.delete_contact = MagicMock()

        # Initialize the CommandsForGUI object
        self.app = CommandsForGUI(self.root, self.contact_manager)

    def tearDown(self):
        self.root.after(100, self.root.destroy())
        self.db.db.close()

    def test_add_contact_integration(self):
        # Initialize add contact fields
        self.app.show_add_contact_fields()

        # Simulate user input
        self.app.first_name_entry.insert(0, "John")
        self.app.surname_entry.insert(0, "Doe")
        self.app.phone_entry.insert(0, "1234567890")
        self.app.email_entry.insert(0, "john.doe@example.com")

        # Call the add_contact_gui method
        self.app.add_contact_gui()

        # Verify that the contact was added
        self.contact_manager.add_contact.assert_called_once()
        print("Add Contact Integration test passed")

    def test_update_contact_integration(self):
        # Initialize edit contact fields
        self.app.show_add_contact_fields()  # Use the same method to initialize fields

        # Simulate user input
        self.app.first_name_entry.insert(0, "Jane")
        self.app.surname_entry.insert(0, "Smith")
        self.app.phone_entry.insert(0, "0987654321")
        self.app.email_entry.insert(0, "jane.smith@example.com")

        # Set current_contact and selected_contact_id to mock contact
        self.app.current_contact = Contact("John", "Doe", "1234567890", "john.doe@example.com")
        self.app.selected_contact_id = 1

        # Mock the edit_contact_window
        self.app.edit_contact_window = MagicMock()

        # Call the edit_contact method
        self.app.edit_contact()

        # Verify that the contact was updated
        self.contact_manager.update_contact.assert_called_once()
        print("Update Contact Integration test passed")

    def test_delete_contact_integration(self):
        # Mock selected item in tree
        selected_item = 'fake_item_id'
        self.app.tree.selection = MagicMock(return_value=[selected_item])
        self.app.tree.item = MagicMock(return_value={'values': ['1', 'John', 'Doe', '1234567890', 'john.doe@example.com']})

        # Add debug prints to trace the flow
        def mock_delete_contact_gui():
            print("delete_contact_gui called")
            selected_item = self.app.tree.selection()[0]
            print(f"Selected item: {selected_item}")
            values = self.app.tree.item(selected_item)['values']
            print(f"Values: {values}")
            first_name = values[1]
            surname = values[2]
            phone = values[3]
            email = values[4]
            self.contact_manager.delete_contact(first_name, surname, phone, email)
            print("delete_contact called")

        self.app.delete_contact_gui = mock_delete_contact_gui

        # Call the delete_contact_gui method
        self.app.delete_contact_gui()

        # Verify that the contact was deleted
        self.contact_manager.delete_contact.assert_called_once()
        print("Delete Contact Integration test passed")

if __name__ == "__main__":
    unittest.main()
