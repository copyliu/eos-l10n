import unittest
from eos import db
from eos.types import Fit, Ship, Module, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBoosterSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sensorBooster = Module(db.getItem("Sensor Booster II"))
        self.signalAmplifier = Module(db.getItem("Signal Amplifier II"))
        self.sensorBooster.state = State.ACTIVE
        self.fit.modules.append(self.sensorBooster)
        self.fit.modules.append(self.signalAmplifier)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sensorBooster.item.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.signalAmplifier.item.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))
