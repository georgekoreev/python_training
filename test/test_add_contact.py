# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="",
                lastname="",
                company="",
                address="",
                home="",
                work="",
                mobile="",
                phone2="",
                email="",
                email2="",
                email3="",
                address2="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10), company=random_string("company", 15),
         address=random_string("address", 20), home=random_string("hometel", 20), work=random_string("worktel", 20),
         mobile=random_string("mobiletel", 20), phone2=random_string("phone2tel", 20), email=random_string("email@", 10),
         email2=random_string("email2@", 10), email3=random_string("email3@", 10), address2=random_string("address2", 20),)
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





