version = "0.2.2.0"
tag = "release"

def test():
    import tests.runTests
    import unittest
    unittest.main(defaultTest="discover", testLoader=tests.runTests.loader)
