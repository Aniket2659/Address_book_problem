import json

class AddressBook:
    def __init__(self):
        self.contacts = []

    def menu(self):
        print('Enter first 5 th option to create address book ')
        print("1. Add contacts to the address book")
        print("2. Edit a contact in the address book")
        print("3. Delete an existing contact")
        print("4. Display contacts")
        print("5. Enter the name of an address book")
        print("6. Display address books")
        print("7. Search for contacts by city")
        print("8. Display all states in list")
        print("9. Display number of contacts ")
        print("10. Display sort contact based on person name ")
        print("11. Display sort contact based on city name ")
        print("12. Save address books to file")
        print("13. Load address books from file")
        choice = int(input("Enter your choice: "))
        return choice

    def create_contact(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        for contact in self.contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                print('This contact already exists')
                return
        
        address = input('Enter your address here: ')
        city = input('Enter your city name: ')
        state = input('Enter your state name: ')
        zip_code = int(input('Enter your zip code: '))
        phone_number = int(input('Enter your phone number: '))
        email = input('Enter your email address: ')
        
        contact = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            'city': city,
            'state': state,
            'zip_code': zip_code,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)

    def edit_contact(self, contact):
        contact['first_name'] = input('Enter new first name: ')
        contact['last_name'] = input('Enter new last name: ')
        contact['address'] = input('Enter new address: ')
        contact['city'] = input('Enter new city name: ')
        contact['state'] = input('Enter new state name: ')
        contact['zip_code'] = int(input('Enter new zip code: '))
        contact['phone_number'] = int(input('Enter new phone number: '))
        contact['email'] = input('Enter new email address: ')

    def del_contact(self):
        full_name1 = input('Enter the full name of the contact to delete: ')
        for contact in self.contacts:
            if full_name1 == f"{contact['first_name']} {contact['last_name']}":
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return
        else:
            print("There is no existing contact")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display")
        else:
            for contact in self.contacts:
                print(contact)
            
    def sort_contacts_byname(self):
        if not self.contacts:
            print("No contacts to display")
        else:
            sorted_contacts = sorted(self.contacts, key=lambda x: x['first_name'])
            for contact in sorted_contacts:
                print(contact)
    
    def sort_contacts_bycity(self):
        if not self.contacts:
            print("No contacts to display")
        else:
            sorted_contacts = sorted(self.contacts, key=lambda x: x['city'])
            for contact in sorted_contacts:
                print(contact)

    def selection(self, choice):
        match choice:
            case 1:
                self.create_contact()
            case 2:
                full_name = input('Enter the full name: ')
                for contact in self.contacts:
                    if full_name == f"{contact['first_name']} {contact['last_name']}":
                        self.edit_contact(contact)
                        break
                else:
                    print('There is no existing contact')
            case 3:
                self.del_contact()
            case 4:
                self.display_contacts()
            case 5:
                m_address_book.create_address_book()
            case 6:
                m_address_book.display_address_book()
            case 7:
                m_address_book.search_contacts_by_city()
            case 8:
                m_address_book.display_all_states()
            case 9:
                print(m_address_book.count_by_state())
            case 10:
                m_address_book.sort_contacts_byname()
            case 11:
                m_address_book.sort_contacts_bycity()
            case 12:
                m_address_book.save_to_file()
            case 13:
                m_address_book.load_from_file()
            case _:
                print("Invalid choice, please try again")


class MultipleAddressBook(AddressBook):
    def __init__(self):
        super().__init__()
        self.address_books = {}

    def create_address_book(self):
        name_address_book = input('Enter the name of the address book to create: ')
        if name_address_book not in self.address_books:
            self.address_books[name_address_book] = []
            print(f"Address book '{name_address_book}' created successfully")
        else:
            print(f"Address book '{name_address_book}' already exists")

    def display_address_book(self):
        if not self.address_books:
            print("No address books to display")
        else:
            for name, contacts in self.address_books.items():
                print(f"Address Book: {name}")
                for contact in contacts:
                    print(contact)

    def add_contact_to_address_book(self):
        name_address_book = input('Enter the name of the address book to add a contact: ')
        if name_address_book in self.address_books:
            self.contacts = self.address_books[name_address_book]
            self.create_contact()
            self.address_books[name_address_book] = self.contacts
        else:
            print(f"Address book '{name_address_book}' does not exist")

    def search_contacts_by_city(self):
        search_city = input('Enter the city name to search for contacts: ')
        results = []
        for book_name, contacts in self.address_books.items():
            for contact in contacts:
                if contact['city'].lower() == search_city.lower():
                    results.append((contact['first_name']))
        
        if results:
            for contact in results:
                print(f"Person name: {contact}")
        else:
            print(f"No contacts found in city '{search_city}'")

    def display_all_states(self):
        states = []
        for contacts in self.address_books.values():
            for contact in contacts:
                states.append(contact['state'])
        
        if states:
            for state in states:
                print(state)
        else:
            print("No states to display")
    
    def count_by_state(self):
        count_states = []
        for contacts in self.address_books.values():
            for contact in contacts:
                count_states.append(contact['state'])
        return len(count_states)

    def save_to_file(self, filename='address_books.json'):
        with open(filename, 'w') as file:
            json.dump(self.address_books, file, indent=4)
        print(f"Address books saved to {filename}")

    def load_from_file(self, filename='address_books.json'):
        try:
            with open(filename, 'r') as file:
                self.address_books = json.load(file)
            print(f"Address books loaded from {filename}")
        except FileNotFoundError:
            print(f"No such file: {filename}")

if __name__ == "__main__":
    m_address_book = MultipleAddressBook()
    while True:
        user_choice = m_address_book.menu()
        if user_choice in [1]:
            m_address_book.add_contact_to_address_book()
        else:
            m_address_book.selection(user_choice)

        exit = input('Do you want to continue (yes/no)? ')
        if exit.lower() == 'no':
            break
