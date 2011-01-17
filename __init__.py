version = "0.2.0.0"
tag = "git"

def test():
    import tests.runTests
    import unittest
    unittest.main(defaultTest="discover", testLoader=tests.runTests.loader)
