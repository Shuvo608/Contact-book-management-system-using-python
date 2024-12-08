from contact_save import load_contacts, save_contacts, validate_contact_input

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()

    try:
        validate_contact_input(name, email, phone, address)
        contacts = load_contacts()

        if phone in contacts:
            print("Error: This phone number is already use")
            return

        contacts[phone] = {"name": name, "email": email, "address": address}
        save_contacts(contacts)
        print(f"Contact for {name} added successfully!")
    except ValueError as e:
        print(f"Input Error: {e}")