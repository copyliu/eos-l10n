from sqlalchemy.orm import validates 
import hashlib

class User(object):
    def __init__(self, username, password, admin):
        self.username = username
        self.encodeAndSetPassword(password)
        self.admin = admin
    
    def encodeAndSetPassword(self, pw):
        h = hashlib.new("sha256")
        h.update(pw.encode())
        self.password = h.hexdigest()
        
    def isPasswordValid(self, pw):
        h = hashlib.new("sha256")
        h.update(pw.encode())
        return self.password == h.hexdigest()
    
    @validates("ID", "username", "password", "admin")
    def validator(self, key, val):
        map = {"ID": lambda val: type(val) == int,
               "username" : lambda val: type(val) == str,
               "password" : lambda val: type(val) == str and len(val) == 64,
               "admin" : lambda val: type(val) == bool}
        
        if map[key](val) == False: raise ValueError(str(val) + " is not a valid value for " + key)
        else: return val