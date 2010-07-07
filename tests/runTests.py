import hashlib, unittest, os, os.path, sys

#Add the good path to sys.path
path = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.append(path)

from model import config

config.debug = False
config.saveddata_connectionstring = "sqlite:///:memory:"

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

def iteratedir(dir, prefix = []):
    for filename in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, filename)):
            iteratedir(os.path.join(dir, filename), prefix + [filename])
        moduleName, ext = os.path.splitext(filename)
        if ext == ".py" and moduleName != "__init__":
            moduleName = '.'.join(prefix + [moduleName])
            module = __import__(moduleName, fromlist = True)
            suite.addTest(loader.loadTestsFromModule(module))

iteratedir(os.path.dirname(__file__))

if __name__ == "__main__":
    unittest.TextTestRunner().run(suite)