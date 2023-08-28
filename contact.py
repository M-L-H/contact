import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, name, new_phone, new_email):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone
                contact.email = new_email
                break

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def save_to_json(self, filename):
        data = []
        for contact in self.contacts:
            data.append({"name": contact.name, "phone": contact.phone, "email": contact.email})
        with open(filename, "w") as file:
            json.dump(data, file)

    def load_from_json(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    contact = Contact(item["name"], item["phone"], item["email"])
                    self.contacts.append(contact)
        except FileNotFoundError:
            pass

def main():
    contact_book = ContactBook()
    contact_book.load_from_json("contacts.json")

    while True:
        print("\n1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. Search Contact\n5. Display Contacts\n6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone, email)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            name = input("Enter name to edit: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contact_book.edit_contact(name, new_phone, new_email)
        elif choice == '3':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '4':
            name = input("Enter name to search: ")
            found_contact = contact_book.search_contact(name)
            if found_contact:
                print(f"Contact found - Name: {found_contact.name}, Phone: {found_contact.phone}, Email: {found_contact.email}")
            else:
                print("Contact not found.")
        elif choice == '5':
            contact_book.display_contacts()
        elif choice == '6':
            contact_book.save_to_json("contacts.json")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

