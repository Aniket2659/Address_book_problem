class AddressBook:
    def __init__(self):
        self.contacts = []

    def menu(self):
        print("1. Add the contacts in address book")
        print("2. Edit a contact in the address book")
        print("3. Delete the existing contact")
        print("4. Display the contact ")
        print("5. Enter name of address book")
        print("6. Display address book")
        choice = int(input("Enter your choice: "))
        return choice

    def create_contact(self):
        first_name = input('enter your first name: ')
        last_name = input('enter your last name: ')
        address = input('enter your address here: ')
        city = input('enter your city name: ')
        state = input('enter your state name: ')
        zip_code = int(input('enter your zip code: '))
        phone_number = int(input('enter your phone number: '))
        email = input('enter your email address: ')
        
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

    def edit_contact(self,contact):
        for contact in self.contacts:
            contact['first_name'] = input('enter new first name ')
            contact['last_name'] = input('enter new last name ')
            contact['address'] = input('enter new address ')
            contact['city'] = input('enter new city name')
            contact['state'] = input('enter new state name ')
            contact['zip_code'] = int(input('enter new zip code '))
            contact['phone_number'] = int(input('enter new phone number '))
            contact['email'] = input('enter new email address')

    def del_contact(self):
        full_name1 = input('enter the full name of the contact to delete: ')
        for contact in self.contacts:
            if full_name1 == f"{contact['first_name']} {contact['last_name']}":
                self.contacts.remove(contact)
        else:
            print("There is no existing contact.")

    def display_contacts(self):
        if not self.contacts:
            print("no contacts to display.")
        else:
            print(self.contacts)



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
                    print('there is no existing contact')
            case 3:
                self.del_contact()
            case 4:
                self.display_contacts()
            case 5:
                m_address_book.create_address_book()
            case 6:
                m_address_book.display_address_book()
            case _:
                print("invalid choice please try again.")


class multiple_address_book(AddressBook):
    def __init__(self):
        super().__init__()

        self.address_books = {}
    
    def create_address_book(self):
        name_address_book=input('enter the name of address book to create:')
        if name_address_book not in self.address_books:
            self.address_books[name_address_book]=address.contacts
            
    
    def display_address_book(self):
        print(self.address_books)



if __name__ == "__main__":
    address = AddressBook()
    m_address_book=multiple_address_book()
    while True:
        user_choice = address.menu()
        address.selection(user_choice)

        exit=input('do you want to continue(yes/no)')
        if exit=='no':
            break
    

