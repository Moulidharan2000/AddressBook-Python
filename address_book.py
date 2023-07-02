import logging


class Contacts:
    def __init__(self, first_name, last_name, city, state, zip_code, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number


class AddressBook:
    def __init__(self):
        self.contacts_dict = {}

    def add_contacts(self, contacts_obj):
        self.contacts_dict.update({contacts_obj.first_name + "," + contacts_obj.last_name: contacts})

    def display(self):
        return self.contacts_dict


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, filename="AddressBook_Logs.log", filemode="w",
                            format="%(asctime)s - %(levelname)s - %(message)s")
        first_name = input("Enter the First Name : ")
        last_name = input("Enter the Last name : ")
        city = input("Enter the City : ")
        state = input("Enter the State : ")
        zip_code = int(input("Enter the Zip Code : "))
        phone_number = int(input("Enter the Phone Number : "))
        contacts = Contacts(first_name, last_name, city, state, zip_code, phone_number)
        address_book = AddressBook()
        address_book.add_contacts(contacts)
        print(address_book.display())
        logging.info(f"Address Book is Created...")
    except Exception as ex:
        print(ex)
