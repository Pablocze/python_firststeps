# -*- coding: utf-8 -*-
from model.contact import Contact
from model.date import  Date


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Paw", middlename = "Share", lastname = "sdfdsfdf", nickname = "gsgs", title = "sfdsf", company = "fgghh", email = "fhjfhjf@mail.com")
    app.contact.create(contact, Date("5", "March", "1990"), Date("11", "april", "2020"))
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



