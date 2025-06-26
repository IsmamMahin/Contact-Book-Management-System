import os
import csv
from menu import menu, wait_for_enter, clear_console
from add_contact import add_contact
from search_contact import search_contact
from view_contact import view_contact
from remove_contact import remove_contact
from save_to_file import save_contacts_to_file, load_contacts_from_file

clear_console()
contacts = load_contacts_from_file()
while True:
#Menu is loaded
    menu()
    choice = input("Enter your choice: ")
    
    try:
        choice = int(choice) # Convert the string to an integer
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue


    if choice == 1:
        add_contact(contacts)
        save_contacts_to_file(contacts)
        wait_for_enter()
        clear_console()


    elif choice == 2:
        view_contact(contacts)
        wait_for_enter()
        clear_console()


    elif choice == 3:
        search_term = input("Enter search term (name/email/phone):")
        search_contact(contacts, search_term)
        wait_for_enter()
        clear_console()


    elif choice == 4:
        contacts = load_contacts_from_file()
        remove_contact(contacts)
        wait_for_enter()
        clear_console()


    elif choice == 5:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        wait_for_enter()
        clear_console()
