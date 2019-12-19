# -*- coding: utf-8 -*-
from model.user import Contact


def test_add_user(app, db, json_contacts, check_ui):
    app.open_home_page()
    old_contacts = db.get_contact_list()
    app.contact.create(json_contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(json_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list_from_table(), key=Contact.id_or_max)