import unittest
from model.types import Implant
from model import db

class TestImplant(unittest.TestCase):
    def test_InvalidImplant(self):
        try:
            i = Implant(db.getItem("Gamma L"))
        except ValueError:
            return
        self.fail("Was expected a ValueError when setting Gamma L as implant, didn't get it")
        
    def test_validImplant(self):
        i = Implant(db.getItem("Halo Omega"))
        self.assertEquals(i.slot, 6)