import csv

# Functions to save contacts from contacts.csv file
def save_contacts_to_file(contacts, filename="contacts.csv"):
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Phone Number', 'Email', 'Address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for phone_num, contact_details in contacts.items():
                writer.writerow({
                    'Name': contact_details.get('name', ''),
                    'Phone Number': phone_num,             
                    'Email': contact_details.get('email', ''),
                    'Address': contact_details.get('address', '')
                })
        print(f"Contacts saved to {filename} successfully.")
    except IOError as e:
        print(f"Error saving contacts to CSV: {e}")

# Functionsload contacts from contacts.csv file
def load_contacts_from_file(filename="contacts.csv"):
    contacts = {}
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone_number = row.get('Phone Number')
                if phone_number:
                    contacts[phone_number] = {
                        'name': row.get('Name', ''),    
                        'email': row.get('Email', ''),
                        'address': row.get('Address', '')
                    }
        print(f"Contacts loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing contacts file found at {filename}. Starting with an empty contact list.")
    except Exception as e:
        print(f"Error loading contacts from CSV: {e}")
    return contacts