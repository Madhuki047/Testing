import unittest
from unittest.mock import patch, MagicMock
import mysql.connector
from ClassDatabase import Database, DatabaseManagement

def normalize_sql(sql):
    return " ".join(sql.split())

class TestDatabase(unittest.TestCase):
    @patch('ClassDatabase.mysql.connector.connect')
    def setUp(self, mock_connect):
        # Mocking the database connection and cursor
        self.mock_db = MagicMock()
        self.mock_cursor = MagicMock()
        mock_connect.return_value = self.mock_db
        self.mock_db.cursor.return_value = self.mock_cursor

        # Initialize the Database object
        self.db = Database()

    def tearDown(self):
        self.db.db.close()

    def test_connect_db(self):
        self.mock_db.cursor.assert_any_call()

    def test_create_table(self):
        self.db.create_table()
        expected_query = """
            CREATE TABLE IF NOT EXISTS contacts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                surname VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL,
                email VARCHAR(255)
            )
        """
        normalized_expected_query = normalize_sql(expected_query)
        actual_calls = [normalize_sql(call[0][0]) for call in self.mock_cursor.execute.call_args_list]
        self.assertIn(normalized_expected_query, actual_calls)

    def test_execute_query_with_values(self):
        query = "INSERT INTO contacts (first_name, surname, phone, email) VALUES (%s, %s, %s, %s)"
        values = ("John", "Doe", "1234567890", "john.doe@example.com")
        self.db.execute_query(query, values)
        self.mock_cursor.execute.assert_any_call(query, values)
        self.mock_db.commit.assert_called_once()

    def test_execute_query_without_values(self):
        query = "SELECT * FROM contacts"
        self.db.execute_query(query)
        self.mock_cursor.execute.assert_any_call(query)
        self.mock_db.commit.assert_called_once()

    def test_fetch_data(self):
        expected_data = [("John", "Doe", "1234567890", "john.doe@example.com")]
        self.mock_cursor.fetchall.return_value = expected_data
        data = self.db.fetch_data()
        self.mock_cursor.execute.assert_any_call("SELECT * FROM contacts")
        self.assertEqual(data, expected_data)

    def test_reassign_ids(self):
        self.db.reassign_ids()
        self.assertEqual(self.mock_cursor.execute.call_count, 4)
        self.mock_db.commit.assert_called_once()

class TestDatabaseManagement(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock(spec=Database)
        self.db_mgmt = DatabaseManagement(self.mock_db)

    def test_add_contact(self):
        contact = MagicMock()
        contact.first_name = "John"
        contact.surname = "Doe"
        contact.phone = "1234567890"
        contact.email = "john.doe@example.com"
        self.db_mgmt.add_contact(contact)
        query = "INSERT INTO contacts (first_name, surname, phone, email) VALUES (%s, %s, %s, %s)"
        values = (contact.first_name, contact.surname, contact.phone, contact.email)
        self.mock_db.execute_query.assert_called_once_with(query, values)

    def test_view_contacts(self):
        self.db_mgmt.view_contacts()
        self.mock_db.fetch_data.assert_called_once()

    def test_delete_contact(self):
        first_name = "John"
        surname = "Doe"
        phone = "1234567890"
        email = "john.doe@example.com"
        self.db_mgmt.delete_contact(first_name, surname, phone, email)
        query = "DELETE FROM contacts WHERE first_name = %s AND surname = %s AND phone = %s AND email = %s"
        values = (first_name, surname, phone, email)
        self.mock_db.execute_query.assert_called_once_with(query, values)
        self.mock_db.reassign_ids.assert_called_once()

    def test_update_contact(self):
        contact = MagicMock()
        contact.first_name = "John"
        contact.surname = "Doe"
        contact.phone = "1234567890"
        contact.email = "john.doe@example.com"
        contact_id = 1
        self.db_mgmt.update_contact(contact, contact_id)
        query = """
        UPDATE contacts SET first_name = %s, surname = %s, phone = %s, email = %s WHERE id = %s
        """
        values = (contact.first_name, contact.surname, contact.phone, contact.email, contact_id)
        self.mock_db.execute_query.assert_called_once_with(query, values)

if __name__ == "__main__":
    unittest.main()
