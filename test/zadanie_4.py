# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_task1(app):
        app.session.login(username="admin", password="secret")
        app.group_creation(Group(name="name", header="noidea", footer="whatimdoing"))
        app.session.logout()


def test_empty(app):
    app.session.login(username="admin", password="secret")
    app.group_creation(Group(name="", header="", footer=""))
    app.session.logout()


def test_signs(app):
    app.session.login(username="admin", password="secret")
    app.group_creation(Group(name="!#@#%%^^#$^", header="@#%#&$$*(!", footer="@%$#^%&**(%^^&%@!$!@"))
    app.session.logout()