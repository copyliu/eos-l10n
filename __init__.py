version = "0.2.0.0"
tag = "Stable"

def test():
    import tests.runTests
    import unittest
    unittest.main(defaultTest="discover", testLoader=tests.runTests.loader)
