import unittest
from eos import db
from eos.types import Fit, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sai = db.getItem("Signal Amplifier II")
        self.sam1 = Module(self.sai)
        self.sam2 = Module(self.sai)
        self.fit.modules.append(self.sam1)
        self.fit.modules.append(self.sam2)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_maxTargetRange(self):
        self.buildTested = 171215
        original = self.fit.ship.item.getAttribute("maxTargetRange")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("maxTargetRange", self.sai.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        expected.boost("maxTargetRange", self.sai.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["maxTargetRange"], self.fit.ship.getModifiedItemAttr("maxTargetRange"))

    def test_maxLockedTargets(self):
        self.buildTested = 171215
        original = self.fit.ship.item.getAttribute("maxLockedTargets")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.increase("maxLockedTargets", self.sai.getAttribute("maxLockedTargetsBonus"))
        expected.increase("maxLockedTargets", self.sai.getAttribute("maxLockedTargetsBonus"))
        self.assertAlmostEquals(expected["maxLockedTargets"], self.fit.ship.getModifiedItemAttr("maxLockedTargets"))
