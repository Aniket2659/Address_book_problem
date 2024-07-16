class AddressBook:
    def __init__(self):
        self.contacts = []

    def menu(self):
        print("1. Add the contacts in address book")
        print("2. Edit a contact in the address book")
        print("3. Delete the existing contact")
        print("4. Display the contact")
        print("5. Enter name of address book")
        print("6. Display address book")
        choice = int(input("Enter your choice: "))
        return choice

    def create_contact(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        for contact in self.contacts:
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                print('this contact already exists')
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
                print("Contact deleted successfully.")
                return
        else:
            print("There is no existing contact.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            for contact in self.contacts:
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
            case _:
                print("Invalid choice, please try again.")


class MultipleAddressBook(AddressBook):
    def __init__(self):
        super().__init__()
        self.address_books = {}

    def create_address_book(self):
        name_address_book = input('Enter the name of address book to create: ')
        if name_address_book not in self.address_books:
            self.address_books[name_address_book] = []
            print(f"Address book '{name_address_book}' created successfully.")
        else:
            print(f"Address book '{name_address_book}' already exists.")

    def display_address_book(self):
        if not self.address_books:
            print("No address books to display.")
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
            print(f"Address book '{name_address_book}' does not exist.")


if __name__ == "__main__":
    m_address_book = MultipleAddressBook()
    while True:
        user_choice = m_address_book.menu()
        if user_choice in [1, 2, 3, 4]:
            m_address_book.add_contact_to_address_book()
        else:
            m_address_book.selection(user_choice)

        exit = input('Do you want to continue (yes/no)? ')
        if exit.lower() == 'no':
            break
