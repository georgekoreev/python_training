# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="Ivan", sname="Ivanov", address="Moscow"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(name="", sname="", address=""))
    app.session.logout()
