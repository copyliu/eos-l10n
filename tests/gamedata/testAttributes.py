import unittest
from eos import db

class TestAttributes(unittest.TestCase):
    def test_AttributeNamesMatch(self):
        i = db.getItem("Gamma L")
        for attrName, attr in i.attributes.iteritems():
            self.assertEquals(attrName, attr.name)

    def test_attributeAmount(self):
        i = db.getItem("Gamma L")
        self.assertEqual(len(i.attributes), 18)

    def test_attributeUnit(self):
        a = db.getAttributeInfo("maxVelocity")
        self.assertEquals(a.unit.name, "Acceleration")
        self.assertEquals(a.unit.displayName, "m/sec")
