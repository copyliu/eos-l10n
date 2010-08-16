import unittest
from eos import db
from eos.types import Fit, Ship, Module, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBooster(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sensorBooster1 = Module(db.getItem("Sensor Booster II"))
        self.sensorBooster2 = Module(db.getItem("Sensor Booster II"))
        self.sensorBooster1.state = State.ACTIVE
        self.sensorBooster2.state = State.ACTIVE
        self.fit.modules.append(self.sensorBooster1)
        self.fit.modules.append(self.sensorBooster2)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("scanResolution", self.sensorBooster1.item.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        expected.boost("scanResolution", self.sensorBooster2.item.getAttribute("scanResolutionBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["scanResolution"], self.fit.ship.getModifiedItemAttr("scanResolution"))

    def test_maxTargetRange(self):
        self.buildTested = 171215
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost("maxTargetRange", self.sensorBooster1.item.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        expected.boost("maxTargetRange", self.sensorBooster2.item.getAttribute("maxTargetRangeBonus"), stackingPenalties = True)
        self.assertAlmostEquals(expected["maxTargetRange"], self.fit.ship.getModifiedItemAttr("maxTargetRange"))
