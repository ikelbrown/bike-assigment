class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        print self.name + "is logged in"
        return self

new_user  = User("Anna","anna@anna.com")
print new_user.email

class User(object):
    name = "Anna"
anna = User()
print "anna's name:", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name

