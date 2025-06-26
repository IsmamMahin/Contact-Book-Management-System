# Function to search a contact

def search_contact(contacts, search_term):
    found_contacts = {}
    for phone_num, details in contacts.items():
        contact_name = details.get('name', '')
        contact_email = details.get('email', '')
        contact_address = details.get('address', '')

        # Check for search_term in name, email, or phone_num 
        if search_term.lower() in contact_name.lower() or \
           search_term.lower() in contact_email.lower() or \
           search_term.lower() in phone_num.lower(): 
            found_contacts[phone_num] = details 

    if found_contacts:
        print("\n=========== SEARCH RESULTS ===========")
        for phone_num_found, details_found in found_contacts.items():
            print(f"Name: {details_found.get('name', 'N/A')}")    
            print(f"Phone: {phone_num_found}")         
            print(f"Email: {details_found.get('email', 'N/A')}")
            print(f"Address: {details_found.get('address', 'N/A')}")
            print("------------------------------------")
        print("====================================")
    else:
        print(f"No contacts found for '{search_term}'.")