# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Paw", lastname="Cze", title="awwww", mobile="123456789", email="aaa@wpa.pl", address="adress"))
        app.session.logout()


def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="", lastname="", title="", mobile="", email="", address=""))
        app.session.logout()