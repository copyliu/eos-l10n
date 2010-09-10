import unittest
from eos.types import Price
import time

class TestPrice(unittest.TestCase):
    def test_valid(self):
        p = Price(1)
        p.time = time.time() - Price.VALIDITY + 1000
        self.assertTrue(p.isValid)

    def test_invalid(self):
        p = Price(1)
        p.time = time.time() - Price.VALIDITY - 1000
        self.assertFalse(p.isValid)
