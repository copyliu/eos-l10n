import hashlib, unittest, os, os.path, sys

#Add the good path to sys.path
path = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.append(path)

from model import config

config.debug = False
config.saveddata_connectionstring = "sqlite:///:memory:"

from model import db
from model.types import User, Character

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

for filename in os.listdir(os.path.dirname(__file__)):
    moduleName, ext = os.path.splitext(filename)
    if ext == ".py" and moduleName != "__init__":
        n = "model.tests." + moduleName
        module = __import__(n, fromlist = True)
        suite.addTest(loader.loadTestsFromModule(module))

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)