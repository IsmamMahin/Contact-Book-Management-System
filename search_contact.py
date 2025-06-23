def search_contact(contacts, search_term):
    #if search_term in contacts:
    #    contact = contacts[search_term]
    #    print("Seach result:")
     #   print(f'Name: {name}')
    #    print(f'Phone number: {phone_number}')
    

    if search_term in contacts:
        contact_details = contacts[search_term]
        print(f"Found contact by Name: {search_term}")
        print(f"  Name: {search_term}") # The search_term itself is the name
        print(f"  Phone number: {contact_details.get('phone_number', 'N/A')}")
        print(f"  Email: {contact_details.get('email', 'N/A')}")
        print(f"  Address: {contact_details.get('address', 'N/A')}")
        return # Exit the function after finding a direct match