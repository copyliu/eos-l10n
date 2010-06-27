import unittest
from ..types.saveddata.fit import ModifiedAttributeDict
from ..db import queries

class TestModifiedAttributeDict(unittest.TestCase):
    def setUp(self):
        self.dict = ModifiedAttributeDict()
        self.i = queries.getItem("125mm Gatling AutoCannon I")
        
    def test_setInvalidOriginal(self):
        try:
            self.dict.original = 1302
        except ValueError:
            return
        self.fail("Set original to an invalid value, expected ValueError")
        
    def test_SetValidOriginal(self):
        self.dict.original = self.i.attributes
        
    def test_OriginalAttributesMatch(self):
        self.dict.original = self.i.attributes
        for key,val in self.dict.iteritems():
            self.assertEqual(val, self.i.attributes[key].value)
            
    def test_ModificationWorks(self):
        self.dict.original = self.i.attributes
        self.dict["hp"] = 5
        self.assertEqual(self.dict["hp"], 5)