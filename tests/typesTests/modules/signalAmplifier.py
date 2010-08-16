import unittest
from eos import db
from eos.types import Fit, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.signalAmplifier1 = Module(db.getItem("Signal Amplifier II"))
        self.signalAmplifier2 = Module(db.getItem("Signal Amplifier II"))
        self.fit.modules.append(self.signalAmplifier1)
        self.fit.modules.append(self.signalAmplifier2)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.signalAmplifier1.item.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.signalAmplifier2.item.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_maxTargetRange(self):
        self.buildTested = 171215
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("maxTargetRange", self.signalAmplifier1.item.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        expected.boost("maxTargetRange", self.signalAmplifier2.item.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["maxTargetRange"], self.fit.ship.getModifiedItemAttr("maxTargetRange"))

    def test_maxLockedTargets(self):
        self.buildTested = 171215
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.increase("maxLockedTargets", self.signalAmplifier1.item.getAttribute("maxLockedTargetsBonus"))
        expected.increase("maxLockedTargets", self.signalAmplifier2.item.getAttribute("maxLockedTargetsBonus"))
        self.assertAlmostEquals(expected["maxLockedTargets"], self.fit.ship.getModifiedItemAttr("maxLockedTargets"))
