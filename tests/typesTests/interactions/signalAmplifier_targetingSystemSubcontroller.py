import unittest
from eos import db
from eos.types import Module, Fit, Ship
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSignalAmplifierTargetingSubsystemSubcontroller(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sai = db.getItem("Signal Amplifier II")
        self.t1tssi = db.getItem("Small Targeting System Subcontroller I")
        self.t2tssi = db.getItem("Small Targeting System Subcontroller II")
        self.sam = Module(self.sai)
        self.t1tssm = Module(self.t1tssi)
        self.t2tssm = Module(self.t2tssi)

    def test_scanResolutionT1(self):
        self.buildTested = 171215
        self.fit.modules.append(self.sam)
        self.fit.modules.append(self.t1tssm)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t1tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_scanResolutionT2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.sam)
        self.fit.modules.append(self.t2tssm)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = False)
        expected.multiply("scanResolution", self.t2tssi.getAttribute("scanResolutionMultiplier"), stackingPenalties = False)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))
