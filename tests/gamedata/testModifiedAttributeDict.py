import unittest
from model.saveddata.fit import ModifiedAttributeDict
from model import db

class TestModifiedAttributeDict(unittest.TestCase):
    def setUp(self):
        self.dict = ModifiedAttributeDict()
        self.i = db.getItem("125mm Gatling AutoCannon I")
        
    def test_SetValidOriginal(self):
        self.dict.original = self.i.attributes
        
    def test_OriginalAttributesMatch(self):
        self.dict.original = self.i.attributes
        for key,val in self.dict.items():
            self.assertEqual(val, self.i.attributes[key].value)
            
    def test_ModificationWorks(self):
        self.dict.original = self.i.attributes
        self.dict["hp"] = 5
        self.assertEqual(self.dict["hp"], 5)