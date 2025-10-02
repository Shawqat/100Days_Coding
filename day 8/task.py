# Phonebook application
def enhanced_phonebook():
    phonebook = {}
    
    while True:
        print("\n=== ENHANCED PHONEBOOK ===")
        print("1. Add contact")
        print("2. View contact")
        print("3. Update contact") 
        print("4. Delete contact")
        print("5. List all contacts")
        print("6. Search contacts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            name = input("Enter contact name: ").title()
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            
            # Store multiple pieces of info for each contact
            phonebook[name] = {
                "phone": phone,
                "email": email
            }
            print(f"Added {name} to phonebook!")
            
        elif choice == "2":
            name = input("Enter contact name to view: ")
            if name in phonebook:
                contact = phonebook[name]
                print(f"\n--- {name} ---")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
            else:
                print(f"Contact '{name}' not found!")
                
        elif choice == "3":
            name = input("Enter contact name to update: ").title()
            if name in phonebook:
                print("Leave blank to keep current value:")
                new_phone = input(f"New phone [{phonebook[name]['phone']}]: ") or phonebook[name]['phone']
                new_email = input(f"New email [{phonebook[name]['email']}]: ") or phonebook[name]['email']
                
                phonebook[name] = {"phone": new_phone, "email": new_email}
                print(f"Updated {name}!")
            else:
                print(f"Contact '{name}' not found!")
                
        elif choice == "4":
            name = input("Enter contact name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Deleted {name} from phonebook!")
            else:
                print(f"Contact '{name}' not found!")
                
        elif choice == "5":
            if not phonebook:
                print("Phonebook is empty!")
            else:
                print("\n--- ALL CONTACTS ---")
                for name, info in phonebook.items():
                    print(f"{name}: {info['phone']} | {info['email']}")
                    
        elif choice == "6":
            search_term = input("Enter name to search: ").title()
            found = False
            for name, info in phonebook.items():
                if search_term in name.lower():
                    print(f"{name}: {info['phone']} | {info['email']}")
                    found = True
            if not found:
                print("No contacts found matching your search.")
                
        elif choice == "7":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

# Run the enhanced phonebook
enhanced_phonebook()