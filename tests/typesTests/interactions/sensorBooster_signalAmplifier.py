import unittest
from eos import db
from eos.types import Fit, Ship, Module, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBoosterSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sbi = db.getItem("Sensor Booster II")
        self.sai = db.getItem("Signal Amplifier II")
        self.sbm = Module(self.sbi)
        self.sam = Module(self.sai)
        self.sbm.state = State.ACTIVE
        self.fit.modules.append(self.sbm)
        self.fit.modules.append(self.sam)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        original = self.fit.ship.item.getAttribute("scanResolution")
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sbi.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.sai.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))
