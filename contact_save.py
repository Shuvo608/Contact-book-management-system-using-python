import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, email, phone, address = line.strip().split("--||--")
                contacts[phone] = {"name": name, "email": email, "address": address}
    return contacts

def save_contacts(contacts):
    """Save contacts"""
    with open(CONTACTS_FILE, "w") as file:
        for phone, details in contacts.items():
            file.write(f"{details['name']}|{details['email']}|{phone}|{details['address']}\n")

def validate_contact_input(name, email, phone, address):
    """Validate contact"""
    if not name.isalpha():
        raise ValueError("Not using any number or any symbol")
    if not phone.isdigit():
        raise ValueError("The phone number is not valid")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email")
    if not address:
        raise ValueError("The address cannot be empty.")