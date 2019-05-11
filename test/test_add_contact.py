# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="Ivan", sname="Ivanov", address="Moscow"))
    #app.session.logout()

def test_add_empty_contact(app):
    #app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="", sname="", address=""))
    #app.session.logout()
