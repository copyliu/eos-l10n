import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.tests.typesTests import calculateBoostMultiplier

class TestSensorBooster(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sb1m = Module(db.getItem("Sensor Booster II"))
        self.sb2m = Module(db.getItem("Sensor Booster II"))
        self.sb1m.state = State.ACTIVE
        self.sb2m.state = State.ACTIVE
        self.fit.modules.append(self.sb1m)
        self.fit.modules.append(self.sb2m)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        original = self.fit.ship.item.attributes["scanResolution"].value
        boostList = []
        boostList.append(self.sb1m.item.attributes["scanResolutionBonus"].value)
        boostList.append(self.sb2m.item.attributes["scanResolutionBonus"].value)
        expected = original * calculateBoostMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("scanResolution"), 3)

    def test_maxTargetRange(self):
        original = self.fit.ship.item.attributes["maxTargetRange"].value
        boostList = []
        boostList.append(self.sb1m.item.attributes["maxTargetRangeBonus"].value)
        boostList.append(self.sb2m.item.attributes["maxTargetRangeBonus"].value)
        expected = original * calculateBoostMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("maxTargetRange"), 3)


