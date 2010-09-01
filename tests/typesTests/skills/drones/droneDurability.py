import unittest
from eos import db
from eos.types import Fit, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDroneDurability(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Drone Durability")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_civilian(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Hobgoblin")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_light(self):
        self.buildTested = 0
        self.testItem = db.getItem("Caldari Navy Hornet")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_medium(self):
        self.buildTested = 0
        self.testItem = db.getItem("Infiltrator II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_heavy(self):
        self.buildTested = 0
        self.testItem = db.getItem("'Augmented' Wasp")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_sentry(self):
        self.buildTested = 0
        self.testItem = db.getItem("Imperial Navy Curator")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testItem = db.getItem("Einherji")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_fighterBomber(self):
        self.buildTested = 0
        self.testItem = db.getItem("Cyclops")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_electronicWarfare(self):
        self.buildTested = 0
        self.testItem = db.getItem("Hobgoblin SD-300")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_combatUtility(self):
        self.buildTested = 0
        self.testItem = db.getItem("Berserker SW-900")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_logistic(self):
        self.buildTested = 0
        self.testItem = db.getItem("Medium Armor Maintenance Bot II")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBonus = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBonus * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_civilianMining(self):
        self.buildTested = 0
        self.testItem = db.getItem("Civilian Mining Drone")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_mining(self):
        self.buildTested = 0
        self.testItem = db.getItem("Mining Drone I")
        self.testDrone = Drone(self.testItem)
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)
