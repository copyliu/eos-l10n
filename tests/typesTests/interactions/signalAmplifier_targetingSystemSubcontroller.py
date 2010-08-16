import unittest
from eos import db
from eos.types import Fit, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalAmplifierTargetingSubsystemSubcontroller(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.signalAmplifier = Module(db.getItem("Signal Amplifier II"))
        self.t1TargetingSystemSubcontroller = Module(db.getItem("Small Targeting System Subcontroller I"))
        self.t2TargetingSystemSubcontroller = Module(db.getItem("Small Targeting System Subcontroller II"))

    def test_scanResolutionT1(self):
        self.buildTested = 171215
        self.fit.modules.append(self.signalAmplifier)
        self.fit.modules.append(self.t1TargetingSystemSubcontroller)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.signalAmplifier.item.getAttribute("scanResolutionBonus"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t1TargetingSystemSubcontroller.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.signalAmplifier)
        self.fit.modules.append(self.t2TargetingSystemSubcontroller)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.signalAmplifier.item.getAttribute("scanResolutionBonus"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t2TargetingSystemSubcontroller.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))
