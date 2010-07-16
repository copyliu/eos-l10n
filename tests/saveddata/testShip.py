import unittest
from model.types import Ship
from model import db
class TestShip(unittest.TestCase):
    def test_clear(self):
        s = Ship(db.getItem("Rifter"))
        orig = s.getModifiedItemAttr("hp")
        s.itemModifiedAttributes["hp"] = 5
        s.clear()
        self.assertEqual(s.getModifiedItemAttr("hp"), orig)