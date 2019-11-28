# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="Paw", lastname="Alk", title="mr", mobile="123123123", email="paw@vp.pl",
                address="ul. zamkowa"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", title="", mobile="", email="", address=""))