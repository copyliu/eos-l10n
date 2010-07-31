import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.tests.typesTests import getStackingPenaltyFactor

class TestSensorBoosterSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.sbi = db.getItem("Sensor Booster II")
        self.sai = db.getItem("Signal Amplifier II")
        self.sbm = Module(self.sbi)
        self.sam = Module(self.sai)
        self.fit = Fit()
        self.sbm.state = State.ACTIVE
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.fit.modules.append(self.sbm)
        self.fit.modules.append(self.sam)
        self.fit.calculateModifiedAttributes()

    def test_scanRes(self):
        original = self.fit.ship.item.attributes["scanResolution"].value
        bonusList = []
        bonusList.append(self.sbi.attributes["scanResolutionBonus"].value/100)
        bonusList.append(self.sai.attributes["scanResolutionBonus"].value/100)
        bonusList = sorted(bonusList, reverse = True)
        expected = original
        for bonusIndex in range(len(bonusList)):
            expected *= 1 + bonusList[bonusIndex]*getStackingPenaltyFactor(bonusIndex)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("scanResolution"), 3)
