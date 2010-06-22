from testQueries import TestQueries
from testFitBasics import TestFitBasics
import unittest

loader = unittest.defaultTestLoader
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromTestCase(TestQueries))
suite.addTest(loader.loadTestsFromTestCase(TestFitBasics))

def test():
    unittest.TextTestRunner(verbosity=2).run(suite)