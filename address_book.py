def menu():
    print("1. Add the contacts in address book")
    choice = int(input("Enter your choice: "))
    return choice

def create_contact():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    address = input('Enter your address here: ')
    city = input('Enter your city name: ')
    state = input('Enter your state name: ')
    zip_code = int(input('Enter your zip code: '))
    phone_number = int(input('Enter your phone number: '))
    email = input('Enter your email address: ')


def selection(choice):
    match choice:
        case 1:
            create_contact()
        case _:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_choice = menu()
    selection(user_choice)
