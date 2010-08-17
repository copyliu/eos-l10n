import unittest
from eos import db
from eos.types import Fit, Ship, Character, Skill, Drone
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestDroneDurability(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testDroneDurability")
        self.skill = db.getItem("Drone Durability")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_civilian(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Civilian Hobgoblin"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_light(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Caldari Navy Hornet"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_medium(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Infiltrator II"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_heavy(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("'Augmented' Wasp"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_sentry(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Imperial Navy Curator"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_fighter(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Einherji"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_fighterBomber(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Cyclops"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_electronicWarfare(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Hobgoblin SD-300"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_combatUtility(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Berserker SW-900"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_logistic(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Medium Armor Maintenance Bot II"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            skillBoost = self.skill.getAttribute(layerBonus)
            expected.boost(layer, skillBoost * self.skillLevel)
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_civilianMining(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Civilian Mining Drone"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)

    def test_mining(self):
        self.buildTested = 0
        self.testDrone = Drone(db.getItem("Mining Drone I"))
        self.fit.drones.append(self.testDrone)
        self.fit.calculateModifiedAttributes()
        expected = ModifiedAttributeDict()
        expected.original = self.testDrone.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"),
                                  ("armorHP", "armorHpBonus"),
                                  ("hp", "hullHpBonus")):
            actual = self.testDrone.getModifiedItemAttr(layer)
            self.assertAlmostEquals(expected[layer], actual)
