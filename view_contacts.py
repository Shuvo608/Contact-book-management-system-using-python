from contact_save import load_contacts

def view_contacts():
    print("\n--- Contact List ---")
    print("------------------------------------")
    contacts = load_contacts()
    print("------------------------------------")

    if not contacts:
        print("No contacts found.")
        return

    for phone, details in contacts.items():
        print(f"Name: {details['name']}")
        print(f"Email: {details['email']}")
        print(f"Phone: {phone}")
        print(f"Address: {details['address']}")
        print("------------------------------------")