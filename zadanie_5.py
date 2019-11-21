# -*- coding: utf-8 -*-
from contact import Contact
from kontakt import Kontakt
import pytest


@pytest.fixture
def kon(request):
    fixture = Kontakt()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addnew(kon):
        kon.login(username="admin", password="secret")
        kon.contact_creation()
        kon.fill_form(Contact(firstname="Pawe", middlename="Piotr", name="Wrob", adress="alko street 5",
        mobilenumber="123123124",email="pab@mail.com", day="1", month="January", year="2000"))
        kon.logout()