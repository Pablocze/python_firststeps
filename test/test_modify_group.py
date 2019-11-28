from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="tak"))
    app.group.modify_first_group(Group(name="imi"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="nie"))
    app.group.modify_first_group(Group(header="ok"))