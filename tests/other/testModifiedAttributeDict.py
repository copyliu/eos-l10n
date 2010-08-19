import unittest
from eos.modifiedAttributeDict import ModifiedAttributeDict
from eos import db

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

    def test_overrideAndCalculate(self):
        self.dict.original = self.i.attributes
        self.dict["hp"] = 5
        self.dict.increase("hp", 5)
        self.assertEqual(self.dict["hp"], 10)

    def test_calculateOverride(self):
        self.dict.original = self.i.attributes
        original = self.dict["hp"]
        self.dict.increase("hp", 10)
        self.dict["hp"] = 5
        self.assertEqual(self.dict["hp"], 15)

    def test_OriginalNone(self):
        self.dict.original = {}
        try:
            self.dict["maeazhtg"]
        except KeyError:
            return
        self.fail("Expected KeyError, didn't get it.")

    def test_force(self):
        self.dict.original = self.i.attributes
        self.dict.force("hp", 9000)
        self.dict.increase("hp",284)
        self.dict.multiply("hp", 2487)
        self.dict["hp"] = 1
        self.assertEqual(self.dict["hp"], 9000)

    def test_newValue(self):
        self.dict.original = {}
        self.dict["test"] = 3
        self.dict.increase("test", 5)
        self.assertEqual(self.dict["test"], 8)

    def test_increaseInexistent(self):
        self.dict.original = {}
        self.dict.increase("test", 5)
        self.assertEquals(self.dict["test"], 5)
