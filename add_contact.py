#Function to add contact
def add_contact(contacts):
    name = input("Enter name: ")

    while True:
        phone_number = input("Enter Phone Number (11 digits): ")

        is_valid_length = False
        is_int = False

        #Check length
        if len(phone_number) == 11:
            is_valid_length = True
        else:
            print("The number you entered is not 11 digits.")

        try:
            int(phone_number) # If it fails, it means non-digits are present.
            is_int = True
        except ValueError:
            print("The number format you typed is invalid.")

        if is_valid_length and is_int:
            break
        else:
            print("Please try again.")

    email = input("Enter email: ")
    address = input("Enter address: ")

    # Check if the phone number already exists
    if phone_number in contacts:
        print(f"Phone number '{phone_number}' already exists for contact '{contacts[phone_number].get('name')}'!!!")
    else:
        # Store the contact
        contacts[phone_number] = {'name': name, 'email': email, 'address': address}
        print("Contact added successfully!")