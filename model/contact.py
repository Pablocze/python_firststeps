from sys import maxsize

class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, title = None, company = None, email = None, id= None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.email = email
        self.id = id

    def __repr__(self):
        return "id - %s, firstname - %s, middlename - %s, lastname - %s, nickname - %s,  title - %s, company - %s, email - %s" % (self.id, self.firstname, self.middlename, self.lastname, self.nickname, self.title,self.company, self.email)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and (self.id == other.id or other.id is None or self.id is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize