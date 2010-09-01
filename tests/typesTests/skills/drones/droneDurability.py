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

    def test_hp_droneCivilian(self):
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

    def test_hp_droneLight(self):
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

    def test_hp_droneMedium(self):
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

    def test_hp_droneHeavy(self):
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

    def test_hp_droneSentry(self):
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

    def test_hp_fighter(self):
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

    def test_hp_fighterBomber(self):
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

    def test_hp_droneElectronicWarfare(self):
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

    def test_hp_droneCombatUtility(self):
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

    def test_hp_droneLogistic(self):
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

    def test_hp_droneMiningCivilian(self):
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

    def test_hp_droneMining(self):
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
