import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBoosterTargetingSubsystemSubcontroller(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sbi = db.getItem("Sensor Booster II")
        self.t1tssi = db.getItem("Small Targeting System Subcontroller I")
        self.t2tssi = db.getItem("Small Targeting System Subcontroller II")
        self.sbm = Module(self.sbi)
        self.t1tssm = Module(self.t1tssi)
        self.t2tssm = Module(self.t2tssi)
        self.sbm.state = State.ACTIVE

    def test_scanResolutionT1(self):
        self.fit.modules.append(self.sbm)
        self.fit.modules.append(self.t1tssm)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sbi.getAttribute("scanResolutionBonus"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT2(self):
        self.fit.modules.append(self.sbm)
        self.fit.modules.append(self.t2tssm)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sbi.getAttribute("scanResolutionBonus"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))
