from model.contact import Contact


def test_modify_contact_name(app):
    #app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(name="New contact"))
    #app.session.logout()


def test_modify_sname(app):
    #app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(sname="New sname"))
    #app.session.logout()