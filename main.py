from menu import menu
from add_contact import add_contact
from search_contact import search_contact
from view_contact import view_contact
from remove_contact import remove_contact
#import json
import csv
from save_to_file import save_contacts_to_file, load_contacts_from_file

contacts = load_contacts_from_file()
while True:
#print("Menu is loaded")
    menu()
    choice = input("Enter your choice: ")
    
    try:
        choice = int(choice) # Convert the string to an integer
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue # Go back to the beginning of the loop


    if choice == 1:
        add_contact(contacts)
        save_contacts_to_file(contacts)

    elif choice == 2:
        view_contact(contacts)

    elif choice == 3:
        search_term = input("Enter search term (name/email/phone):")
        search_contact(contacts, search_term)

    elif choice == 4:
        contacts = load_contacts_from_file()
        remove_contact(contacts)

    elif choice == 5:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
