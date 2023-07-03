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

    def details(self):
        return self.last_name, self.city, self.state, self.zip_code, self.phone_number


class AddressBook:
    def __init__(self, ab_name):
        self.contacts_dict = {}
        self.ab_name = ab_name

    def add_contacts(self, contacts_obj):
        self.contacts_dict.update({contacts_obj.first_name: contacts_obj.details()})

    def update_contacts(self, contacts_obj):
        self.contacts_dict.update({contacts_obj.first_name: contacts_obj.details()}) and print(
            "Contact Updated...") if contacts_obj.first_name in self.contacts_dict else print(
            "No Contacts Found...")

    def delete_contacts(self, first_name):
        self.contacts_dict.pop(first_name) and print(
            "Contacts Deleted...") if first_name in self.contacts_dict else print("No Contacts Found...")

    def display(self):
        for i in self.contacts_dict:
            print(i, " : ", self.contacts_dict.get(i))


class Multiple_AddressBook:

    def __init__(self):
        self.multiple_dict = {}

    def add_ab(self, addressbook_obj):
        self.multiple_dict.update({addressbook_obj.ab_name: addressbook_obj})

    def update_ab(self, addressbook_obj):
        self.multiple_dict.update({addressbook_obj.ab_name: addressbook_obj}) and print(
            "Address Book Updated...") if addressbook_obj.ab_name in self.multiple_dict else print(
            "No Address Book Found...")

    def delete_ab(self, ab_name):
        self.multiple_dict.pop(ab_name) and print(
            "Address Book Deleted...") if ab_name in self.multiple_dict else print("No Address Book Found...")

    def get_addressbook(self):
        for i, j in self.multiple_dict.items():
            print(i, " : ", len(j.contacts_dict))


class Multiple_AddressBook:

    def __init__(self):
        self.multiple_dict = {}

    def add_ab(self, addressbook_obj):
        self.multiple_dict.update({addressbook_obj.ab_name: addressbook_obj})

    def update_ab(self, addressbook_obj):
        self.multiple_dict.update({addressbook_obj.ab_name: addressbook_obj}) and print(
            "Address Book Updated...") if addressbook_obj.ab_name in self.multiple_dict else print(
            "No Address Book Found...")

    def delete_ab(self, ab_name):
        self.multiple_dict.pop(ab_name) and print(
            "Address Book Deleted...") if ab_name in self.multiple_dict else print("No Address Book Found...")

    def get_addressbook(self):
        for i, j in self.multiple_dict.items():
            print(i, " : ", j)


def _add_details():
    ab_name = input("Enter the Address Book Name : ")
    address_book = multiple_ab.multiple_dict.get(ab_name)
    if not address_book:
        address_book = AddressBook(ab_name)
    first_name = input("Enter the First Name : ")
    last_name = input("Enter the Last name : ")
    city = input("Enter the City : ")
    state = input("Enter the State : ")
    zip_code = int(input("Enter the Zip Code : "))
    phone_number = int(input("Enter the Phone Number : "))
    contacts = Contacts(first_name, last_name, city, state, zip_code, phone_number)
    return contacts, address_book


def _add():
    contacts, address_book = _add_details()
    address_book.add_contacts(contacts)
    multiple_ab.add_ab(address_book)


def _update():
    contacts, address_book = _add_details()
    address_book.update_contacts(contacts)
    multiple_ab.update_ab(address_book)


def _delete_contacts():
    ab_name = input("Enter the Address Book Name : ")
    address_book = multiple_ab.multiple_dict.get(ab_name)
    if address_book:
        first_name = input("Enter the First Name : ")
        address_book.delete_contacts(first_name)
    else:
        print("No Address Book Found...")


def _delete_addressbook():
    ab_name = input("Enter the Address Book Name : ")
    multiple_ab.delete_ab(ab_name)


def _display_contacts():
    ab_name = input("Enter the Address Book Name : ")
    address_book = multiple_ab.multiple_dict.get(ab_name)
    print("No Address Book Found") if not address_book else address_book.display()


def _display_addressbook():
    print("No Address Book Present") if not multiple_ab.multiple_dict else multiple_ab.get_addressbook()


if __name__ == '__main__':
    try:
        multiple_ab = Multiple_AddressBook()
        while True:
            choice = int(input(
                "\n1.Add Contacts\n2.Update Contacts\n3.Delete Contacts\n4.Delete Address Book\n5.Display Contacts\n6.Display Address Book\n0.Exit\nEnter the Option : "))
            choice_dict = {1: _add, 2: _update, 3: _delete_contacts, 4: _delete_addressbook, 5: _display_contacts,
                           6: _display_addressbook}
            if choice == 0:
                print("Exited...")
                break
            else:
                choice_dict.get(choice)()
            logging.info(f"Address Book is Created...")
    except Exception as ex:
        print(ex)
        logging.exception(ex)
