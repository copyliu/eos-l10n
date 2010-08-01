import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sai = db.getItem("Signal Amplifier II")
        self.sa1m = Module(self.sai)
        self.sa2m = Module(self.sai)
        self.fit.modules.append(self.sa1m)
        self.fit.modules.append(self.sa2m)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_maxTargetRange(self):
        original = self.fit.ship.item.getAttribute("maxTargetRange")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("maxTargetRange", self.sai.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        expected.boost("maxTargetRange", self.sai.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["maxTargetRange"], self.fit.ship.getModifiedItemAttr("maxTargetRange"))

    def test_maxLockedTargets(self):
        original = self.fit.ship.item.getAttribute("maxLockedTargets")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.increase("maxLockedTargets", self.sai.getAttribute("maxLockedTargetsBonus"))
        expected.increase("maxLockedTargets", self.sai.getAttribute("maxLockedTargetsBonus"))
        self.assertAlmostEquals(expected["maxLockedTargets"], self.fit.ship.getModifiedItemAttr("maxLockedTargets"))
