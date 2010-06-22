import unittest
from .. import db

class TestQueries(unittest.TestCase):
    def test_getItem(self):
        i = db.getItem("Gamma L")
        self.assertEqual(i.name, "Gamma L")
        self.assertEqual(i.ID, 261)
        
    def test_searchItems(self):
        i = db.searchItems("Gamma L")
        self.assertEqual(len(i), 7)
        
    def test_getVariations(self):
        i = db.getItem("Gamma L")
        vars = db.getVariations(i)
        for var in vars:
            self.assertEqual(var.metaGroup.parent, i)