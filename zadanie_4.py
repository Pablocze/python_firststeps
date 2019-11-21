# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_task1(app):
        app.login(username="admin", password="secret")
        app.group_creation(Group(name="name", header="noidea", footer="whatimdoing"))
        app.logout()


def test_empty(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(name="", header="", footer=""))
    app.logout()


def test_signs(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(name="!#@#%%^^#$^", header="@#%#&$$*(!", footer="@%$#^%&**(%^^&%@!$!@"))
    app.logout()