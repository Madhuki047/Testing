import unittest
from unittest.mock import MagicMock, patch
from ClassDatabase import Database, DatabaseManagement

class TestDatabaseIntegration(unittest.TestCase):
    @patch('ClassDatabase.mysql.connector.connect')
    def setUp(self, mock_connect):
        # Mock the database connection and cursor
        self.mock_db = MagicMock()
        self.mock_cursor = MagicMock()
        mock_connect.return_value = self.mock_db
        self.mock_db.cursor.return_value = self.mock_cursor

        # Initialize the Database and DatabaseManagement objects
        self.db = Database()
        self.db_mgmt = DatabaseManagement(self.db)

    def tearDown(self):
        self.db.db.close()

    def test_add_and_view_contact(self):
        # Reset mock to ignore previous calls
        self.mock_cursor.reset_mock()

        # Mock contact details
        contact = MagicMock()
        contact.first_name = "John"
        contact.surname = "Doe"
        contact.phone = "1234567890"
        contact.email = "john.doe@example.com"

        # Add the contact and verify the query
        self.db_mgmt.add_contact(contact)
        query = "INSERT INTO contacts (first_name, surname, phone, email) VALUES (%s, %s, %s, %s)"
        values = (contact.first_name, contact.surname, contact.phone, contact.email)
        self.mock_cursor.execute.assert_any_call(query, values)
        self.mock_db.commit.assert_called()

        # View contacts and verify the query
        self.mock_cursor.fetchall.return_value = [(1, "John", "Doe", "1234567890", "john.doe@example.com")]
        contacts = self.db_mgmt.view_contacts()
        self.mock_cursor.execute.assert_any_call("SELECT * FROM contacts")
        self.assertEqual(contacts, [(1, "John", "Doe", "1234567890", "john.doe@example.com")])

    def test_update_contact(self):
        # Reset mock to ignore previous calls
        self.mock_cursor.reset_mock()

        # Mock contact details
        contact = MagicMock()
        contact.first_name = "Jane"
        contact.surname = "Smith"
        contact.phone = "0987654321"
        contact.email = "jane.smith@example.com"
        contact_id = 1

        # Update the contact and verify the query
        self.db_mgmt.update_contact(contact, contact_id)
        query = """
        UPDATE contacts SET first_name = %s, surname = %s, phone = %s, email = %s WHERE id = %s
        """
        values = (contact.first_name, contact.surname, contact.phone, contact.email, contact_id)
        self.mock_cursor.execute.assert_any_call(query, values)
        self.mock_db.commit.assert_called()

    def test_delete_contact(self):
        # Reset mock to ignore previous calls
        self.mock_cursor.reset_mock()

        # Mock contact details
        first_name = "John"
        surname = "Doe"
        phone = "1234567890"
        email = "john.doe@example.com"

        # Delete the contact and verify the query
        self.db_mgmt.delete_contact(first_name, surname, phone, email)
        query = "DELETE FROM contacts WHERE first_name = %s AND surname = %s AND phone = %s AND email = %s"
        values = (first_name, surname, phone, email)
        self.mock_cursor.execute.assert_any_call(query, values)
        self.mock_db.commit.assert_called()

    def test_reassign_ids(self):
        # Reset mock to ignore previous calls
        self.mock_cursor.reset_mock()

        # Reassign IDs and verify the queries
        self.db.reassign_ids()
        self.assertEqual(self.mock_cursor.execute.call_count, 3)
        self.mock_db.commit.assert_called()

if __name__ == "__main__":
    unittest.main()
