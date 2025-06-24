# save_contacts.py
import csv

def save_contacts_to_file(contacts, filename="contacts.csv"):
    """Saves the contacts dictionary to a CSV file."""
    try:
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'Phone Number', 'Email', 'Address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for name, details in contacts.items():
                writer.writerow({
                    'Name': name,
                    'Phone Number': details.get('phone_number', ''),
                    'Email': details.get('email', ''),
                    'Address': details.get('address', '')
                })
        print(f"Contacts saved to {filename} successfully.")
    except IOError as e:
        print(f"Error saving contacts to CSV: {e}")

def load_contacts_from_file(filename="contacts.csv"):
    """Loads contacts from a CSV file into a dictionary."""
    contacts = {}
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get('Name')
                if name:
                    contacts[name] = {
                        'phone_number': row.get('Phone Number', ''),
                        'email': row.get('Email', ''),
                        'address': row.get('Address', '')
                    }
        print(f"Contacts loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing contacts file found at {filename}. Starting with an empty contact list.")
    except Exception as e:
        print(f"Error loading contacts from CSV: {e}")
    return contacts