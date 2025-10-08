from dataclasses import dataclass, asdict
from typing import Dict, List, Optional


@dataclass
class Contact:
    name: str
    phone: str
    email: str
    group: str = "General"


class ContactManager:
    def __init__(self):
        self.contacts: Dict[str, Contact] = {}
        self.groups: Dict[str, List[str]] = {}

    # ---------------------------
    # Internal Helper Methods
    # ---------------------------
    def _add_to_group(self, name: str, group: str):
        self.groups.setdefault(group, []).append(name)

    def _remove_from_group(self, name: str, group: str):
        if group in self.groups and name in self.groups[group]:
            self.groups[group].remove(name)
            if not self.groups[group]:
                del self.groups[group]

    # ---------------------------
    # Core Contact Operations
    # ---------------------------
    def add_contact(self, contact: Contact) -> bool:
        if contact.name in self.contacts:
            return False

        self.contacts[contact.name] = contact
        self._add_to_group(contact.name, contact.group)
        return True

    def find_contact(self, name: str) -> Optional[Contact]:
        return self.contacts.get(name)

    def list_contacts(self, group: Optional[str] = None) -> List[Contact]:
        if group:
            names = self.groups.get(group, [])
            return [self.contacts[n] for n in names]
        return list(self.contacts.values())

    def update_contact(
        self,
        name: str,
        new_name: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        group: Optional[str] = None,
    ) -> bool:
        contact = self.contacts.get(name)
        if not contact:
            return False

        # Handle rename
        if new_name and new_name != name:
            self.contacts[new_name] = self.contacts.pop(name)
            contact.name = new_name
            self._remove_from_group(name, contact.group)
            self._add_to_group(new_name, contact.group)

        # Update fields
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        if group and group != contact.group:
            self._remove_from_group(contact.name, contact.group)
            contact.group = group
            self._add_to_group(contact.name, group)

        return True

    def delete_contact(self, name: str) -> bool:
        contact = self.contacts.pop(name, None)
        if not contact:
            return False
        self._remove_from_group(name, contact.group)
        return True

    def get_statistics(self):
        return {
            "total": len(self.contacts),
            "by_group": {group: len(names) for group, names in self.groups.items()},
        }
    

def main():
    manager = ContactManager()

    menu = {
        "1": "Add Contact",
        "2": "Edit Contact",
        "3": "Find Contact",
        "4": "List All Contacts",
        "5": "List Contacts by Group",
        "6": "Delete Contact",
        "7": "Statistics",
        "8": "Exit",
    }

    while True:
        print("\n" + "="*50)
        print("📇 CONTACT MANAGEMENT SYSTEM")
        for key, label in menu.items():
            print(f"{key}. {label}")
        print("="*50)

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            name = input("Name: ").strip().lower()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            group = input("Group (default: General): ").strip() or "General"
            added = manager.add_contact(Contact(name, phone, email, group))
            print("✅ Contact added!" if added else "⚠️ Contact already exists!")

        elif choice == "2":
            name = input("Enter contact name to edit: ").strip().lower()
            new_name = input("New name (leave blank to keep): ").strip().lower() or None
            phone = input("New phone (leave blank to keep): ").strip() or None
            email = input("New email (leave blank to keep): ").strip() or None
            group = input("New group (leave blank to keep): ").strip() or None
            updated = manager.update_contact(name, new_name, phone, email, group)
            print("✅ Updated!" if updated else "❌ Contact not found.")

        elif choice == "3":
            name = input("Enter name: ").strip().lower()
            c = manager.find_contact(name)
            print(asdict(c) if c else "❌ Contact not found.")

        elif choice == "4":
            for contact in manager.list_contacts():
                print(f"👤 {contact.name}")
                print(f"   📞 Phone: {contact.phone}")
                print(f"   📧 Email: {contact.email}")
                print(f"   🏷️  Group: {contact.group}")
                print("-" * 30)

        elif choice == "5":
            group = input("Enter group name: ").strip()
            contacts = manager.list_contacts(group)
            if contacts:
                for contact in contacts:
                    print(f"👤 {contact.name}")
                    print(f"   📞 Phone: {contact.phone}")
                    print(f"   📧 Email: {contact.email}")
                    print(f"   🏷️  Group: {contact.group}")
                    print("-" * 30)
            else:
                print("❌ Group not found or empty.")

        elif choice == "6":
            name = input("Enter name: ").strip().lower()
            deleted = manager.delete_contact(name)
            print("✅ Deleted!" if deleted else "❌ Not found.")

        elif choice == "7":
            stats = manager.get_statistics()
            print(f"Total contacts: {stats['total']}")
            for g, n in stats["by_group"].items():
                print(f"{g}: {n}")

        elif choice == "8":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
