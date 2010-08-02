import unittest
from model.types import Ship
from model import db
from copy import deepcopy
class TestShip(unittest.TestCase):
    def test_clear(self):
        s = Ship(db.getItem("Rifter"))
        orig = s.getModifiedItemAttr("hp")
        s.itemModifiedAttributes["hp"] = 5
        s.clear()
        self.assertEqual(s.getModifiedItemAttr("hp"), orig)

    def test_copy(self):
        s = Ship(db.getItem("Rifter"))
        c = deepcopy(s)

        self.assertNotEquals(id(s), id(c))
        self.assertEquals(s.item, c.item)