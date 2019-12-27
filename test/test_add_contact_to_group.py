# -*- coding: utf-8 -*-
import random
import time
from model.group import Group
from model.user import Contact


def test_add_contact_to_group(app, orm_db):
    app.open_home_page()
    groups = app.group.groups_without_empty_names(orm_db.get_group_list())
    
    len_before = len(groups)
    for gr in range(len_before):
        if len(orm_db.get_contacts_not_in_group(groups[len_before-gr-1])) == 0:
            groups.pop(len_before-gr-1)

    if len(groups) == 0:
        app.contact.create(Contact(firstname="t_a_c_t_g User", lastname="t_a_c_t_g User last name",
                                   companyname="t_a_c_t_g user center2m", address="t_a_c_t_g User street, 21"))

        groups = app.group.groups_without_empty_names(orm_db.get_group_list())
        if len(groups) == 0:
            app.group.create(Group(name="t_a_c_t_g Group"))
            groups = app.group.groups_without_empty_names(orm_db.get_group_list())

    group = random.choice(groups)
    group_db_id = group.id
    cont_not_in_gr_list = orm_db.get_contacts_not_in_group(Group(id=group_db_id))

    user_to_add = random.choice(cont_not_in_gr_list)

    index = 0
    app.wd.get(app.base_url + "group.php")
    time.sleep(1)
    app.open_home_page()
    time.sleep(1)

    for c in range(len(orm_db.get_contact_list())):
        ui_id = app.contact.find_user_id_by_index(c)
        if ui_id == user_to_add.id:
            index = c
    app.contact.add_to_group(index, group_db_id)
    cont_list_after = None
    cont_list_after = orm_db.get_contacts_not_in_group(Group(id=group_db_id))

    if cont_list_after is not None:

        for u in range(len(cont_list_after)):
            if cont_list_after[u].id == user_to_add.id:
                assert False
            assert True
    assert True


