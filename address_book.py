import logging

logging.basicConfig(level=logging.INFO, filename="AddressBook_Logs.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


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
        self.contacts_dict.update({contacts_obj.first_name: contacts_obj})

    def update_contacts(self, contacts_obj):
        self.contacts_dict.update({contacts_obj.first_name: contacts_obj}) and print(
            "Contact Updated...") if contacts_obj.first_name in self.contacts_dict else print(
            "No Contacts Found...")

    def delete_contacts(self, first_name):
        self.contacts_dict.pop(first_name) and print(
            "Contact Deleted...") if first_name in self.contacts_dict else print("No Contacts Found...")

    def display(self):
        for i, j in self.contacts_dict.items():
            print(i, " : ", j)


def _add_details():
    first_name = input("Enter the First Name : ")
    last_name = input("Enter the Last name : ")
    city = input("Enter the City : ")
    state = input("Enter the State : ")
    zip_code = int(input("Enter the Zip Code : "))
    phone_number = int(input("Enter the Phone Number : "))
    contacts = Contacts(first_name, last_name, city, state, zip_code, phone_number)
    return contacts


def _add():
    contacts = _add_details()
    address_book.add_contacts(contacts)


def _update():
    contacts = _add_details()
    address_book.update_contacts(contacts)


def _delete():
    first_name = input("Enter the First Name : ")
    address_book.delete_contacts(first_name)


def _display():
    address_book.display()


if __name__ == '__main__':
    try:
        address_book = AddressBook()
        while True:
            choice = int(input(
                "\n1.Add Contacts\n2.Update Contacts\n3.Delete Contacts\n4.Display Contacts\n0.Exit\nEnter the Option : "))
            choice_dict = {1: _add, 2: _update, 3: _delete, 4: _display}
            if choice == 0:
                print("Exited...")
                break
            else:
                choice_dict.get(choice)()
            logging.info(f"Address Book is Created...")
    except Exception as ex:
        print(ex)
        logging.exception(ex)
