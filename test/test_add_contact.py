# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_contact(Contact(name="Ivan", sname="Ivanov", address="Moscow"))

def test_add_empty_contact(app):
    app.contact.create_contact(Contact(name="", sname="", address=""))
