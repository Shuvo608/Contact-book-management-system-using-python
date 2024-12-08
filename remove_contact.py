from contact_save import load_contacts, save_contacts

def remove_contact():
    print("\n--- Remove Contact ---")
    phone = input("Enter the phone number of the contact to remove: ").strip()
    contacts = load_contacts()

    if phone in contacts:
        removed_contact = contacts.pop(phone)
        save_contacts(contacts)
        print(f"Contact for {removed_contact['name']} removed successfully!")
    else:
        print("Error: No contact found.")