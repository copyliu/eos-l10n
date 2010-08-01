import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.tests.typesTests import calculateBoostMultiplier

class TestSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.sa1m = Module(db.getItem("Signal Amplifier II"))
        self.sa2m = Module(db.getItem("Signal Amplifier II"))
        self.fit.modules.append(self.sa1m)
        self.fit.modules.append(self.sa2m)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        original = self.fit.ship.item.attributes["scanResolution"].value
        boostList = []
        boostList.append(self.sa1m.item.attributes["scanResolutionBonus"].value)
        boostList.append(self.sa2m.item.attributes["scanResolutionBonus"].value)
        expected = original * calculateBoostMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("scanResolution"), 3)

    def test_maxTargetRange(self):
        original = self.fit.ship.item.attributes["maxTargetRange"].value
        boostList = []
        boostList.append(self.sa1m.item.attributes["maxTargetRangeBonus"].value)
        boostList.append(self.sa2m.item.attributes["maxTargetRangeBonus"].value)
        expected = original * calculateBoostMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("maxTargetRange"), 3)

    def test_maxLockedTargets(self):
        original = self.fit.ship.item.attributes["maxLockedTargets"].value
        expected = original + self.sa1m.item.attributes["maxLockedTargetsBonus"].value + self.sa2m.item.attributes["maxLockedTargetsBonus"].value
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("maxLockedTargets"), 3)
