from sqlalchemy.orm import validates
import hashlib
import string
import random

class User(object):
    def __init__(self, username, password = None, admin = False):
        self.username = username
        if password != None: self.encodeAndSetPassword(password)
        self.admin = admin

    def encodeAndSetPassword(self, pw):
        h = hashlib.new("sha256")
        r = random.seed()
        salt = "".join([random.choice(string.letters) for _ in xrange(32)])
        h.update(pw)
        h.update(salt)
        self.password = ("%s%s" % (h.hexdigest(), salt))

    def isPasswordValid(self, pw):
        if self.password == None: return False
        salt = self.password[-32:]
        h = hashlib.new("sha256")
        h.update(pw)
        h.update(salt)
        return self.password == (u"%s%s" % (h.hexdigest(), salt))

    @validates("ID", "username", "password", "admin")
    def validator(self, key, val):
        map = {"ID": lambda val: isinstance(val, int),
               "username" : lambda val: isinstance(val, basestring),
               "password" : lambda val: isinstance(val, basestring) and len(val) == 96,
               "admin" : lambda val: isinstance(val, bool)}

        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val
