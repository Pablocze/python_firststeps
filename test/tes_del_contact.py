def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_first_contact()
    app.session.logout()