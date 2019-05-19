from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(name="New contact"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_sname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(sname="New sname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)