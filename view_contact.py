# Function to view contacts
def view_contact(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        print("\n=========== ALL CONTACTS ===========")
        for phone_number, details in contacts.items():
            name = details.get('name', 'N/A')
            email = details.get('email', 'N/A')
            address = details.get('address', 'N/A')

            print(f"Name: {name}")
            print(f"Phone: {phone_number}")
            print(f"Email: {email}")
            print(f"Address: {address}")
            print("------------------------------------")
        print("====================================")