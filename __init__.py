def test():
    import tests.runTests
    import unittest
    unittest.main(defaultTest="discover", testLoader=tests.runTests.loader)
