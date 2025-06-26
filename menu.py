import os
#Menu of the system
def menu():
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!")
    print("=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")

def wait_for_enter(prompt="Press Enter to continue..."):
    #Pauses the program execution until the user presses Enter.
    input(prompt)

#clears the screen
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
