from contact_save import load_contacts

def search_contact():
    print("\n--- Search Contact ---")
    print("------------------------------------")
    query = input("Enter name, email, or phone to search: ").strip().lower()
    contacts = load_contacts()
    print("------------------------------------")

    results = [
        details for phone, details in contacts.items()
        if query in details['name'].lower() or query in details['email'].lower() or query == phone
    ]

    if results:
        print(f"\nFound {len(results)} result(s):")
        for result in results:
            print(f"Name: {result['name']}")
            print(f"Email: {result['email']}")
            print(f"Phone: {result['phone']}")
            print(f"Address: {result['address']}")
            print("------------------------------------")
    else:
        print("No contacts matching")