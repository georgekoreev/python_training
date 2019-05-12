from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(name="New contact"))

def test_modify_sname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modify_first_contact(Contact(sname="New sname"))