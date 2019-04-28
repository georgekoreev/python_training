# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import Application_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="Ivan", sname="Ivanov", address="Moscow"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(name="", sname="", address=""))
    app.logout()
