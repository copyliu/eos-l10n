import unittest
from eos import db
from eos.types import Fit, Ship, Module, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestSensorBooster(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.testItem = db.getItem("Sensor Booster II")
        self.testMod1 = Module(self.testItem)
        self.testMod2 = Module(self.testItem)
        self.testMod1.state = State.ACTIVE
        self.testMod2.state = State.ACTIVE
        self.fit.modules.append(self.testMod1)
        self.fit.modules.append(self.testMod2)
        self.fit.calculateModifiedAttributes()

    def test_scanResolution(self):
        self.buildTested = 171215
        bonusAttrName = "scanResolutionBonus"
        targetAttrName = "scanResolution"
        penalize = True
        bonusAttrVal = self.testItem.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        expected.boost(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_maxTargetRange(self):
        self.buildTested = 171215
        bonusAttrName = "maxTargetRangeBonus"
        targetAttrName = "maxTargetRange"
        penalize = True
        bonusAttrVal = self.testItem.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        expected.boost(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
