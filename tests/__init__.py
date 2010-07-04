from .. import config
config.debug = False
config.saveddata_connectionstring = "sqlite:///:memory:"

__all__ = ["testFitBasics", "testModifiedAttributeDict", "testModuleBasics", "testQueries", "testSavedDataBasics"]

from model import db
from model.types import User, Character
import hashlib
import unittest

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

for modulename in __all__:
    n = "model.tests." + modulename
    module = __import__(n, fromlist = True)
    suite.addTest(loader.loadTestsFromModule(module))

def test():
    unittest.TextTestRunner().run(suite)