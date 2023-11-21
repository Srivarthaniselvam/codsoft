class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name, self.phone_number, self.email, self.address = name, phone_number, email, address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone_number]
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def run_contact_manager():
    contact_manager = ContactManager()

    while True:
        print("\n Welcome to Contact Management System")
        print("1. Add Contact\n2. View Contacts\n3. Search Contacts\n4. Update Contact\n5. Delete Contact\nType 'exit' to Exit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            contact_manager.add_contact(Contact(input("Name: "), input("Phone number: "), input("Email: "), input("Address: ")))
            print("Contact added successfully!")

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = contact_manager.search_contacts(query)
            print("Search Results:" if results else "No matching contacts found.")
            [print(f"{i}. {contact.name} - {contact.phone_number}") for i, contact in enumerate(results, start=1)]

        elif choice == "4":
            contact_manager.view_contacts()
            try:
                index = int(input("Enter index of the contact to update: ")) - 1
                contact_manager.update_contact(index, Contact(input("New Name: "), input("New Phone number: "), input("New Email: "), input("New Address: ")))
                print("Contact updated successfully!")
            except (ValueError, IndexError):
                print("Invalid input or index.")

        elif choice == "5":
            contact_manager.view_contacts()
            try:
                index = int(input("Enter index of the contact to delete: ")) - 1
                contact_manager.delete_contact(index)
                print("Contact deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid input or index.")

        elif choice == "exit":
            print(".............Closing Contact Management System............")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

run_contact_manager()
