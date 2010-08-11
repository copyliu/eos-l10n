import unittest
from eos import db
from eos.types import Module, Fit, Ship
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestTargetingSubsystemSubcontroller(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.t1tssi = db.getItem("Small Targeting System Subcontroller I")
        self.t2tssi = db.getItem("Small Targeting System Subcontroller II")
        self.t1tssm1 = Module(self.t1tssi)
        self.t1tssm2 = Module(self.t1tssi)
        self.t2tssm1 = Module(self.t2tssi)
        self.t2tssm2 = Module(self.t2tssi)

    #T1 and T2 rigs have different effects for scanning resolution boost,
    #so we have to test them separately
    def test_scanResolutionT1(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t1tssm1)
        self.fit.modules.append(self.t1tssm2)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t2tssm1)
        self.fit.modules.append(self.t2tssm2)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT1T2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t1tssm1)
        self.fit.modules.append(self.t2tssm1)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_shieldCapacity(self):
        self.buildTested = 171215
        self.fit.modules.append(self.t1tssm1)
        self.fit.modules.append(self.t2tssm2)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("shieldCapacity")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("shieldCapacity", self.t1tssi.getAttribute("drawback"), stackingPenalties = False)
        expected.boost("shieldCapacity", self.t2tssi.getAttribute("drawback"), stackingPenalties = False)
        self.assertAlmostEquals(expected["shieldCapacity"], self.fit.ship.getModifiedItemAttr("shieldCapacity"))
