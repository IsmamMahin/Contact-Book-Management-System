#Fuction to delete contact
def remove_contact(contacts):
    name_to_remove = input("Enter the name of the contact to remove: ")

    # Find all contacts that match the entered name
    matching_contacts = {}
    for phone, details in contacts.items():
        if name_to_remove.lower() in details.get('name', '').lower():
            matching_contacts[phone] = details 
            
    if not matching_contacts:
        print(f"No contact found with the name '{name_to_remove}'.")
    elif len(matching_contacts) == 1:
        # If only one contact matches the name, remove it directly
        phone_to_delete = list(matching_contacts.keys())[0]
        del contacts[phone_to_delete]
        print(f"Contact '{name_to_remove}' ({phone_to_delete}) removed successfully.")
    else:
        # If multiple contacts have the same name, prompt for phone number
        print(f"Multiple contacts found with the name '{name_to_remove}':")
        for phone, details in matching_contacts.items():
            print(f"- Name: {details.get('name')}, Phone: {phone}, Email: {details.get('email')}")

        phone_number_to_remove = input("Enter the phone number of the specific contact to remove: ")

        if phone_number_to_remove in matching_contacts:
            del contacts[phone_number_to_remove]
            print(f"Contact '{name_to_remove}' with phone number '{phone_number_to_remove}' removed successfully.")
        else:
            print(f"No contact found with name '{name_to_remove}' and phone number '{phone_number_to_remove}'.")