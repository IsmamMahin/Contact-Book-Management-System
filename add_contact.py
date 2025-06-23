def add_contact(contact):
    name = input("Enter name:")
    if name in contact:
        print(f'Contact name {name} already exists!!!')
    else:
        phone_number = input("Enter Phone Number:")
        email = input("Enter email:")
        address = input("Enter address:")
        contact[name] = {'phone_number': phone_number, 'email': email, 'address': address}
        print("Contact added successfully!")