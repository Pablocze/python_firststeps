# -*- coding: utf-8 -*-
import random
from model.user import Contact


def test_del_some_user(app, db, check_ui):
    # we remove 4 users to compensate 4 created
    for i in range(4):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="FIRST User first name", lastname="FIRST User last name", companyname="FIRST user center2m", address="FIRST User street, 21", id=None))
        old_contacts = db.get_contact_list()
        user = random.choice(old_contacts)
        db_id = user.id
        index = None
        # Выясняем, какой ui index у выбранного контакта
        for c in range(len(old_contacts)):
            ui_id = app.contact.find_user_id_by_index(c)
            if ui_id == db_id:
                index = c
        app.contact.delete_user_by_index(index)
        new_contacts = db.get_contact_list()
        old_contacts.remove(user)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list_from_table(),
                                                                         key=Contact.id_or_max)