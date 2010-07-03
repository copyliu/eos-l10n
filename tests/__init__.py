from .. import config
from model import db
from model.types import User, Character
import hashlib
from .testQueries import TestQueries
from .testFitBasics import TestFitBasics
from .testModuleBasics import TestModuleBasics
from .testModifiedAttributeDict import TestModifiedAttributeDict
from .testSavedDataBasics import TestSavedDataBasics
import unittest
config.debug = False

#Database setup
config.saveddata_connectionstring = "sqlite:///:memory:"
#Setup a test db, put some stuff in it
db.saveddata_meta.create_all()

#Add some test data
h = hashlib.new("sha1")
h.update("test")  
u = User("test", h.hexdigest(), False)
c = Character("TESTY")
c.owner = u
db.saveddata_session.add(c)
db.saveddata_session.flush()
        


loader = unittest.defaultTestLoader
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromTestCase(TestQueries))
suite.addTest(loader.loadTestsFromTestCase(TestFitBasics))
suite.addTest(loader.loadTestsFromTestCase(TestModuleBasics))
suite.addTest(loader.loadTestsFromTestCase(TestModifiedAttributeDict))
suite.addTest(loader.loadTestsFromTestCase(TestSavedDataBasics))

def test():
    unittest.TextTestRunner().run(suite)