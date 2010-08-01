import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBooster(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sbi = db.getItem("Sensor Booster II")
        self.sb1m = Module(self.sbi)
        self.sb2m = Module(self.sbi)
        self.sb1m.state = State.ACTIVE
        self.sb2m.state = State.ACTIVE
        self.fit.modules.append(self.sb1m)
        self.fit.modules.append(self.sb2m)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sbi.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.sbi.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_maxTargetRange(self):
        original = self.fit.ship.item.getAttribute("maxTargetRange")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("maxTargetRange", self.sbi.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        expected.boost("maxTargetRange", self.sbi.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["maxTargetRange"], self.fit.ship.getModifiedItemAttr("maxTargetRange"))
