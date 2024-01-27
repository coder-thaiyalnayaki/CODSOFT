import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print(f"\nContact '{name}' added successfully!")

def view_contacts(contacts):
    print("\n===== Contact List =====")
    for name, contact_info in contacts.items():
        print(f"{name}: {contact_info['phone']}")

def search_contact(contacts):
    query = input("\nEnter contact name or phone number to search: ")
    found = False

    for name, contact_info in contacts.items():
        if query in (name, contact_info['phone']):
            print(f"\nContact Information for '{name}':")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            found = True

    if not found:
        print("\nContact not found.")

def update_contact(contacts):
    name = input("\nEnter the name of the contact to update: ")

    if name in contacts:
        print(f"\nCurrent contact information for '{name}':")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")

        contacts[name]['phone'] = input("\nEnter new phone number: ")
        contacts[name]['email'] = input("Enter new email address: ")
        contacts[name]['address'] = input("Enter new address: ")

        print(f"\nContact '{name}' updated successfully!")
    else:
        print("\nContact not found.")

def delete_contact(contacts):
    name = input("\nEnter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print(f"\nContact '{name}' deleted successfully!")
    else:
        print("\nContact not found.")

def contact_management():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Management =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("\nExiting Contact Management. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_management()
