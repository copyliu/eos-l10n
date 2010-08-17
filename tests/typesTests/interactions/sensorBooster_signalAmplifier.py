import unittest
from eos import db
from eos.types import Fit, Ship, Module, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBoosterSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.testItem1 = db.getItem("Sensor Booster II")
        self.testItem2 = db.getItem("Signal Amplifier II")
        self.testMod1 = Module(self.testItem1)
        self.testMod2 = Module(self.testItem2)
        self.testMod1.state = State.ACTIVE
        self.fit.modules.append(self.testMod1)
        self.fit.modules.append(self.testMod2)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        bonusAttrName = "scanResolutionBonus"
        targetAttrName = "scanResolution"
        penalize = True
        bonusAttrVal1 = self.testItem1.getAttribute(bonusAttrName)
        bonusAttrVal2 = self.testItem2.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, bonusAttrVal1, stackingPenalties = penalize)
        expected.boost(targetAttrName, bonusAttrVal2, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxTargetRange(self):
        self.buildTested = 0
        bonusAttrName = "maxTargetRangeBonus"
        targetAttrName = "maxTargetRange"
        penalize = True
        bonusAttrVal1 = self.testItem1.getAttribute(bonusAttrName)
        bonusAttrVal2 = self.testItem2.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, bonusAttrVal1, stackingPenalties = penalize)
        expected.boost(targetAttrName, bonusAttrVal2, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
