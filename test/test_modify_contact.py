from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="New contact", sname="New sname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    contact.sname = old_contacts[0].sname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_sname(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(name="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(sname="New sname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
