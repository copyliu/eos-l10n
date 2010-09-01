import unittest
from eos import db
from eos.types import Fit, Character, Skill, Implant, Booster, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestTurretDestabilization(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Turret Destabilization")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_trackingDisruptor(self):
        self.buildTested = 0
        self.testItem = db.getItem("Balmer Series Tracking Disruptor I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        skillBonus = self.skill.getAttribute("scanSkillEwStrengthBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for turretMod in ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus"):
            expected.boost(turretMod, skillBonus * self.skillLevel)
            actual = self.testMod.getModifiedItemAttr(turretMod)
            self.assertAlmostEquals(expected[turretMod], actual)

    def test_trackingLink(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Tycoon' Tracking Link I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for turretMod in ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus"):
            actual = self.testMod.getModifiedItemAttr(turretMod)
            self.assertAlmostEquals(expected[turretMod], actual)

    def test_otherMod(self):
        self.buildTested = 0
        self.testItem = db.getItem("Domination Tracking Enhancer")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for turretMod in ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus"):
            actual = self.testMod.getModifiedItemAttr(turretMod)
            self.assertAlmostEquals(expected[turretMod], actual)

    def test_implantTrackingSpeed(self):
        self.buildTested = 0
        self.testItem = db.getItem("Hardwiring - Eifyr and Co. 'Gunslinger' AX-2")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "trackingSpeedBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_implantMaxRange(self):
        self.buildTested = 0
        self.testItem = db.getItem("Low-grade Harvest Alpha")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRangeBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.multiply(targetAttrName, expected["implantSetORE"])
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_implantFalloff(self):
        self.buildTested = 0
        self.testItem = db.getItem("Hardwiring - Zainou 'Deadeye' ZGC100")
        self.testImplant = Implant(self.testItem)
        self.fit.implants.append(self.testImplant)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloffBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testImplant.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_shipMaxRange(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Thrasher"))
        self.fit.calculateModifiedAttributes()
        targetAttrName = "maxRangeBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.fit.ship.item.attributes
        actual = self.fit.ship.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_boosterFalloff(self):
        self.buildTested = 0
        self.testItem = db.getItem("Standard Sooth Sayer Booster")
        self.testBooster = Booster(self.testItem)
        self.fit.boosters.append(self.testBooster)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "falloffBonus"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testBooster.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
