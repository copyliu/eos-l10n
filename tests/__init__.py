from .. import config
config.debug = False

from testQueries import TestQueries
from testFitBasics import TestFitBasics
from testModuleBasics import TestModuleBasics
import unittest


loader = unittest.defaultTestLoader
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromTestCase(TestQueries))
suite.addTest(loader.loadTestsFromTestCase(TestFitBasics))
suite.addTest(loader.loadTestsFromTestCase(TestModuleBasics))

def test():
    unittest.TextTestRunner(verbosity=2).run(suite)