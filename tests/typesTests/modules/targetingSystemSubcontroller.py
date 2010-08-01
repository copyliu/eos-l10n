import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.t1tssi = db.getItem("Small Targeting System Subcontroller I")
        self.t2tssi = db.getItem("Small Targeting System Subcontroller II")
        self.t1tss1m = Module(self.t1tssi)
        self.t1tss2m = Module(self.t1tssi)
        self.t2tss1m = Module(self.t2tssi)
        self.t2tss2m = Module(self.t2tssi)

    #T1 and T2 rigs have different effects for scanning resolution boost,
    #so we have to test them separately
    def test_scanResolutionT1(self):
        self.fit.modules.append(self.t1tss1m)
        self.fit.modules.append(self.t1tss2m)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT2(self):
        self.fit.modules.append(self.t2tss1m)
        self.fit.modules.append(self.t2tss2m)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_shieldCapacity(self):
        self.fit.modules.append(self.t1tss1m)
        self.fit.modules.append(self.t2tss2m)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("shieldCapacity")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("shieldCapacity", self.t1tssi.getAttribute("drawback"), stackingPenalties = False)
        expected.boost("shieldCapacity", self.t2tssi.getAttribute("drawback"), stackingPenalties = False)
        self.assertAlmostEquals(expected["shieldCapacity"], self.fit.ship.getModifiedItemAttr("shieldCapacity"))
