# search_contact.py
def search_contact(contacts, search_term):
    found_contacts = {}
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or \
           search_term.lower() in details.get('email', '').lower() or \
           search_term.lower() in details.get('phone_number', '').lower():
            found_contacts[name] = details

    if found_contacts:
        print("\n=========== SEARCH RESULTS ===========")
        for name, details in found_contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details.get('phone_number', 'N/A')}")
            print(f"Email: {details.get('email', 'N/A')}")
            print(f"Address: {details.get('address', 'N/A')}")
            print("------------------------------------")
        print("====================================")
    else:
        print(f"No contacts found for '{search_term}'.")