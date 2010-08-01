import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.tests.typesTests import calculateBoostMultiplier

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
        original = self.fit.ship.item.attributes["scanResolution"].value
        boostList = []
        boostList.append(self.sbi.attributes["scanResolutionBonus"].value)
        boostList.append(self.sai.attributes["scanResolutionBonus"].value)
        expected = original * calculateBoostMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("scanResolution"), 3)
