from address_book import Contacts, AddressBook, Multiple_AddressBook
import pytest


@pytest.fixture
def contacts():
    return Contacts("Raj", "kumar", "bangalore", "Karnataka", 2352235, 123526668523)


@pytest.fixture
def address_book():
    return AddressBook("Friends")


@pytest.fixture
def multiple_ab():
    return Multiple_AddressBook()


def test_add_contact(contacts, address_book):
    assert len(address_book.contacts_dict) == 0
    address_book.add_contacts(contacts)
    assert len(address_book.contacts_dict) == 1


def test_update_contact(contacts, address_book):
    address_book.add_contacts(contacts)
    assert len(address_book.contacts_dict) == 1
    assert address_book.contacts_dict["Raj"]['last_name'] == "kumar"
    contacts = Contacts("Raj", "takur", "mumbai", "maharastra", 235124, 1251562346)
    address_book.update_contacts(contacts)
    assert address_book.contacts_dict["Raj"]['last_name'] == "takur"


def test_delete_contact(contacts, address_book):
    address_book.add_contacts(contacts)
    assert len(address_book.contacts_dict) == 1
    address_book.delete_contacts(contacts.first_name)
    assert len(address_book.contacts_dict) == 0


def test_add_multiple_contacts(contacts, address_book, multiple_ab):
    assert len(multiple_ab.multiple_dict) == 0
    address_book.add_contacts(contacts)
    multiple_ab.add_ab(address_book)
    assert len(multiple_ab.multiple_dict) == 1


def test_update_multiple_contacts(contacts, address_book, multiple_ab):
    address_book.add_contacts(contacts)
    multiple_ab.add_ab(address_book)
    assert len(multiple_ab.multiple_dict) == 1
    assert address_book.contacts_dict["Raj"]['last_name'] == "kumar"
    contacts = Contacts("Raj", "takur", "mumbai", "maharastra", 235124, 1251562346)
    address_book.update_contacts(contacts)
    multiple_ab.update_ab(address_book)
    assert multiple_ab.multiple_dict["Friends"]


def test_delete_multiple_contacts(contacts, address_book, multiple_ab):
    address_book.add_contacts(contacts)
    multiple_ab.add_ab(address_book)
    assert len(multiple_ab.multiple_dict) == 1
    address_book.delete_contacts(contacts.first_name)
    multiple_ab.delete_ab(address_book.ab_name)
    assert len(multiple_ab.multiple_dict) == 0
