from .. import config
config.debug = False
config.saveddata_connectionstring = "sqlite:///:memory:"

__all__ = ["testFitBasics", "testModifiedAttributeDict", "testModuleBasics", "testQueries", "testSavedDataBasics"]
from model import db
from model.types import User, Character
import sys
import hashlib
import unittest

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

for modulename in __all__:
    n = "model.tests." + modulename
    module = __import__(n)
    suite.addTest(loader.loadTestsFromModule(sys.modules[n]))

def test():
    unittest.TextTestRunner().run(suite)