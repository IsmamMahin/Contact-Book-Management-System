def view_contact(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        print("\n=========== ALL CONTACTS ===========")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details.get('phone_number', 'N/A')}")
            print(f"Email: {details.get('email', 'N/A')}")
            print(f"Address: {details.get('address', 'N/A')}")
            print("------------------------------------")
        print("====================================")