# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", lastname="Ivanov", address="Moscow",
                      company="Google", home="123454", work="5464722",
                      mobile="4672392", phone2="676273",
                      email="kotiki@mail.ru", address2="Magadan")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(name="", sname="", address="")
#    app.contact.create_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




