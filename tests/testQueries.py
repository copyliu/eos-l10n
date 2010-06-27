import unittest
from ..db import queries

class TestQueries(unittest.TestCase):
    def test_getItem(self):
        i = queries.getItem("Gamma L")
        self.assertEqual(i.name, "Gamma L")
        self.assertEqual(i.ID, 261)
        
    def test_searchItems(self):
        i = queries.searchItems("Gamma L")
        self.assertEqual(len(i), 7)
        
    def test_getVariations(self):
        i = queries.getItem("Gamma L")
        vars = queries.getVariations(i)
        for var in vars:
            self.assertEqual(var.metaGroup.parent, i)