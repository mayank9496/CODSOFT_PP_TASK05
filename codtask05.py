class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, search_term, updated_contact):
        found_contacts = self.search_contact(search_term)
        if found_contacts:
            for contact in found_contacts:
                contact.name = updated_contact.name
                contact.phone_number = updated_contact.phone_number
                contact.email = updated_contact.email
                contact.address = updated_contact.address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, search_term):
        found_contacts = self.search_contact(search_term)
        if found_contacts:
            for contact in found_contacts:
                self.contacts.remove(contact)
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nSelect an option:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Found Contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contacts found.")
        elif choice == '4':
            search_term = input("Enter name or phone number of contact to update: ")
            updated_name = input("Enter updated name: ")
            updated_phone_number = input("Enter updated phone number: ")
            updated_email = input("Enter updated email: ")
            updated_address = input("Enter updated address: ")
            updated_contact = Contact(updated_name, updated_phone_number, updated_email, updated_address)
            contact_book.update_contact(search_term, updated_contact)
        elif choice == '5':
            search_term = input("Enter name or phone number of contact to delete: ")
            contact_book.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
