# project Contact Book
# Add, view, and remove contacts (name, phone number).

contacts = ["Ahmed: 01025325484", "Ali: 01025325485", "Omar: 01025325486"]

def show_contacts():
    print("Contacts List:")
    for contact in contacts:
        print(contact)

def add_contact():
    try:
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        if len(phone) != 11:
            raise ValueError("Phone number must be 11 digits.")
        else:
            contacts.append(f"{name}: {phone}")
            print(f"Contact {name} added.")
    except Exception as e:
        print(f"Error adding contact: {e}")

def remove_contact():
    try:
        name = input("Enter contact name to remove: ")
        for contact in contacts:
            if contact.startswith(name + ":"):
                contacts.remove(contact)
                print(f"Contact {name} removed.")
                return
        print(f"Contact {name} not found.")
    except Exception as e:
        print(f"Error removing contact: {e}")

def edit_contact():
    try:
        name = input("Enter contact name to edit: ")
        for i, contact in enumerate(contacts):
            if contact.startswith(name + ":"):
                new_name = input("Enter new contact name: ")
                new_phone = input("Enter new contact phone number: ")
                contacts[i] = f"{new_name}: {new_phone}"
                print(f"Contact {name} updated to {new_name}.")
                return
        print(f"Contact {name} not found.")
    except Exception as e:
        print(f"Error editing contact: {e}")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Edit Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            show_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()