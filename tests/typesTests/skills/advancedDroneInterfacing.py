import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestAdvancedDroneInterfacing(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testAdvancedDroneInterfacing")
        self.adii = db.getItem("Advanced Drone Interfacing")
        self.adil = 5
        self.char.addSkill(Skill(self.adii, self.adil))
        self.fit.character = self.char
        self.dcui = db.getItem("Drone Control Unit I")
        self.dcum = Module(self.dcui)
        self.fit.modules.append(self.dcum)
        self.fit.calculateModifiedAttributes()

    def test_dcuMaxGroupActive(self):
        self.buildTested = 173608
        original = self.dcum.item.getAttribute("maxGroupActive")
        expected = ModifiedAttributeDict()
        expected.original = self.dcum.item.attributes
        expected.increase("maxGroupActive", 1 * self.adil)
        self.assertAlmostEquals(expected["maxGroupActive"], self.dcum.getModifiedItemAttr("maxGroupActive"))
