from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="Anna", lastname="Wana", title="Pani", mobile="358358358", email="bbb@kk.com",
                address="ul. mazowiecka zabrze"))
    app.session.logout()