# remove_contact.py
def remove_contact(contacts):
    """Removes a contact from the contacts dictionary."""
    name_to_remove = input("Enter the name of the contact to remove: ")
    if name_to_remove in contacts:
        del contacts[name_to_remove]
        print(f"Contact '{name_to_remove}' removed successfully.")
    else:
        print(f"Contact '{name_to_remove}' not found.")