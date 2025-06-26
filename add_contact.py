#Function to add contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    # Check if the phone number already exists
    if phone_number in contacts:
        print(f"Phone number '{phone_number}' already exists for contact '{contacts[phone_number].get('name')}'!!!")
    else:
        # Store the contact with phone_number as the key
        contacts[phone_number] = {'name': name, 'email': email, 'address': address}
        print("Contact added successfully!")