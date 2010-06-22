from testQueries import TestQueries
import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromTestCase(TestQueries))

def test():
    unittest.TextTestRunner(verbosity=2).run(suite)