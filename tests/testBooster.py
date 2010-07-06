import unittest
from model import db
from model.types import Booster

class TestBooster(unittest.TestCase):
    def test_SetInvalidBooster(self):
        try:
            b = Booster(db.getItem("Gamma L"))
        except ValueError:
            return
        self.fail("Expected a ValueError when trying to use Gamma L as a booster")
        
    def test_setValidBooster(self):
        b = Booster(db.getItem("Strong Drop Booster"))
        self.assertEquals(2, b.slot)
        i = 0
        for _ in b.iterSideEffects():
            i+= 1
            
        self.assertEquals(4, i)