# -*- coding: utf-8 -*-
import random
from model.group import Group
from data.groups import modgroupdata


def test_modify_groups(app, db, check_ui):
    for mod_gr in modgroupdata:
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="FIRST group", header="11 first group", footer="22 first group"))
        group_to_modify = mod_gr
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        app.group.modify_group_by_id(group_to_modify, group.id)
        new_groups = db.get_group_list()
        # вписываем модифицированную группу в выбранный элемент списка old_group
        group.name = group_to_modify.name
        group.header = group_to_modify.header
        group.footer = group_to_modify.footer
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



#def test_modify_group_header(app):
 #   old_groups = app.group.get_group_list()
 #    if app.group.count() == 0:
 #       app.group.create(Group(name="nie"))
 #   app.group.modify_first_group(Group(header="ok"))
 #   new_groups = app.group.get_group_list()
 #   assert len(old_groups) == len(new_groups)
