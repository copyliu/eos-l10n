import unittest
from eos import db
from eos.types import Fit, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestTargetingSubsystemSubcontroller(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.testItemT1 = db.getItem("Small Targeting System Subcontroller I")
        self.testItemT2 = db.getItem("Small Targeting System Subcontroller II")
        self.testModT1_1 = Module(self.testItemT1)
        self.testModT1_2 = Module(self.testItemT1)
        self.testModT2_1 = Module(self.testItemT2)
        self.testModT2_2 = Module(self.testItemT2)

    # T1 and T2 rigs have different effects for scanning resolution boost,
    # so we have to test them separately
    def test_scanResolutionT1(self):
        self.buildTested = 171215
        self.fit.modules.append(self.testModT1_1)
        self.fit.modules.append(self.testModT1_2)
        self.fit.calculateModifiedAttributes()
        bonusAttrName = "scanResolutionMultiplier"
        targetAttrName = "scanResolution"
        penalize = True
        bonusAttrVal = self.testItemT1.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        expected.multiply(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanResolutionT2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.testModT2_1)
        self.fit.modules.append(self.testModT2_2)
        self.fit.calculateModifiedAttributes()
        bonusAttrName = "scanResolutionMultiplier"
        targetAttrName = "scanResolution"
        penalize = True
        bonusAttrVal = self.testItemT2.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        expected.multiply(targetAttrName, bonusAttrVal, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_scanResolutionT1T2(self):
        self.buildTested = 171215
        self.fit.modules.append(self.testModT1_1)
        self.fit.modules.append(self.testModT2_1)
        self.fit.calculateModifiedAttributes()
        bonusAttrName = "scanResolutionMultiplier"
        targetAttrName = "scanResolution"
        penalize = False
        bonusAttrVal1 = self.testItemT1.getAttribute(bonusAttrName)
        bonusAttrVal2 = self.testItemT2.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.multiply(targetAttrName, bonusAttrVal1, stackingPenalties = penalize)
        expected.multiply(targetAttrName, bonusAttrVal2, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_shieldCapacity(self):
        self.buildTested = 171215
        self.fit.modules.append(self.testModT1_1)
        self.fit.modules.append(self.testModT2_1)
        self.fit.calculateModifiedAttributes()
        bonusAttrName = "drawback"
        targetAttrName = "shieldCapacity"
        penalize = False
        bonusAttrVal1 = self.testItemT1.getAttribute(bonusAttrName)
        bonusAttrVal2 = self.testItemT2.getAttribute(bonusAttrName)
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        expected.boost(targetAttrName, bonusAttrVal1, stackingPenalties = penalize)
        expected.boost(targetAttrName, bonusAttrVal2, stackingPenalties = penalize)
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
