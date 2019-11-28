from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="Monika", lastname="Kowal"))
    app.contact.modify_first_contact(
        Contact(firstname="Ola", lastname="Ola", title="mrs", mobile="111111111", email="ola@to.pl",
                address="Gdansk"))