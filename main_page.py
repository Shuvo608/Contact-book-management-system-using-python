from add_contact import add_contact
from view_contacts import view_contacts
from remove_contact import remove_contact
from search_contact import search_contact

def main_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            print("----- Goodbye!-----")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    print("Welcome to the Contact Book Management System!")
    main_menu()