import unittest
from eos import db
from eos.types import Fit, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestTargetingSubsystemSubcontroller(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.t1TargetingSystemSubcontroller1 = Module(db.getItem("Small Targeting System Subcontroller I"))
        self.t1TargetingSystemSubcontroller2 = Module(db.getItem("Small Targeting System Subcontroller I"))
        self.t2TargetingSystemSubcontroller1 = Module(db.getItem("Small Targeting System Subcontroller II"))
        self.t2TargetingSystemSubcontroller2 = Module(db.getItem("Small Targeting System Subcontroller II"))

    # T1 and T2 rigs have different effects for scanning resolution boost,
    # so we have to test them separately
    def test_scanResolutionT1(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t1TargetingSystemSubcontroller1)
        self.fit.modules.append(self.t1TargetingSystemSubcontroller2)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t1TargetingSystemSubcontroller1.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        expected.multiply("scanResolution", self.t1TargetingSystemSubcontroller2.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t2TargetingSystemSubcontroller1)
        self.fit.modules.append(self.t2TargetingSystemSubcontroller2)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t2TargetingSystemSubcontroller1.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        expected.multiply("scanResolution", self.t2TargetingSystemSubcontroller2.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT1T2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t1TargetingSystemSubcontroller1)
        self.fit.modules.append(self.t2TargetingSystemSubcontroller1)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t1TargetingSystemSubcontroller1.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t2TargetingSystemSubcontroller1.item.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_shieldCapacity(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t1TargetingSystemSubcontroller1)
        self.fit.modules.append(self.t2TargetingSystemSubcontroller1)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("shieldCapacity", self.t1TargetingSystemSubcontroller1.item.getAttribute("drawback"), stackingPenalties = False)
        expected.boost("shieldCapacity", self.t2TargetingSystemSubcontroller1.item.getAttribute("drawback"), stackingPenalties = False)
        self.assertAlmostEquals(expected["shieldCapacity"], self.fit.ship.getModifiedItemAttr("shieldCapacity"))
