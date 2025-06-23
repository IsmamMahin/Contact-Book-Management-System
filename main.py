from menu import menu
from add_contact import add_contact
from search_contact import search_contact

contacts = {}
while True:
#print("Menu is loaded")
    menu()
    choice = int(input("Enter your choice: "))
    
    # try:
    #     choice = int(choice_input) # Convert the string to an integer
    # except ValueError:
    #     print("Invalid input. Please enter a number.")
    #     continue # Go back to the beginning of the loop


    if choice == 1:
        print("DEBUG: Calling add_contact...") # Diagnostic print
        add_contact(contacts)

    elif choice == 3:
        search_term = input("Enter search term (name/email/phone):")
        search_contact(contacts, search_term)

