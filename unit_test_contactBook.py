# Unit testing
import unittest
from THEcontactBOOK import Contact

class TestContact(unittest.TestCase):

    def test_contact_initialization(self):
        first_name = "John"
        surname = "Doe"
        phone = "1234567890"
        email = "john.doe@example.com"
        
        contact = Contact(first_name, surname, phone, email)

        self.assertEqual(contact.first_name, first_name)
        self.assertEqual(contact.surname, surname)
        self.assertEqual(contact.phone, phone)
        self.assertEqual(contact.email, email)

if __name__ == "__main__":
    unittest.main()