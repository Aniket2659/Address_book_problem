class AddressBook:
    def __init__(self):
        self.contacts = []

    def menu(self):
        print("1. Add the contacts in address book")
        choice = int(input("Enter your choice: "))
        return choice

    def create_contact(self):
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        address = input('Enter your address here: ')
        city = input('Enter your city name: ')
        state = input('Enter your state name: ')
        zip_code = input('Enter your zip code: ')
        phone_number = input('Enter your phone number: ')
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

    def selection(self, choice):
        match choice:
            case 1:
                self.create_contact()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    address_book = AddressBook()
    user_choice = address_book.menu()
    address_book.selection(user_choice)
