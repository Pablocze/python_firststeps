from model.contact import Contact
from model.date import Date
from random import randrange

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("TIMMY"), Date("20", "March", "1990"), Date("20", "June", "2000"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname = "bbb", lastname = "aaaa", nickname = "ccc", title = "dgsgs", company = "aadsdas", email = "adasdsdssX@mail.com")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact, Date("20", "april", "1800"), Date("4", "March", "2003"))
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)