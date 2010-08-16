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
        self.civilianHobgoblin = Drone(db.getItem("Civilian Hobgoblin"))
        self.caldariNavyHornet = Drone(db.getItem("Caldari Navy Hornet"))
        self.t2Infiltrator = Drone(db.getItem("Infiltrator II"))
        self.augmentedWasp = Drone(db.getItem("'Augmented' Wasp"))
        self.imperialNavyCurator = Drone(db.getItem("Imperial Navy Curator"))
        self.einherji = Drone(db.getItem("Einherji"))
        self.cyclops = Drone(db.getItem("Cyclops"))
        self.sdHobgoblin = Drone(db.getItem("Hobgoblin SD-300"))
        self.swBerserker = Drone(db.getItem("Berserker SW-900"))
        self.t2MediumArmorMaintenanceBot = Drone(db.getItem("Medium Armor Maintenance Bot II"))
        self.civilianMining = Drone(db.getItem("Civilian Mining Drone"))
        self.t1Mining = Drone(db.getItem("Mining Drone I"))
        self.fit.drones.append(self.civilianHobgoblin)
        self.fit.drones.append(self.caldariNavyHornet)
        self.fit.drones.append(self.t2Infiltrator)
        self.fit.drones.append(self.augmentedWasp)
        self.fit.drones.append(self.imperialNavyCurator)
        self.fit.drones.append(self.einherji)
        self.fit.drones.append(self.cyclops)
        self.fit.drones.append(self.sdHobgoblin)
        self.fit.drones.append(self.swBerserker)
        self.fit.drones.append(self.t2MediumArmorMaintenanceBot)
        self.fit.drones.append(self.civilianMining)
        self.fit.drones.append(self.t1Mining)
        self.fit.calculateModifiedAttributes()

    def test_civilian(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.civilianHobgoblin.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.civilianHobgoblin.getModifiedItemAttr(layer))

    def test_light(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.caldariNavyHornet.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.caldariNavyHornet.getModifiedItemAttr(layer))

    def test_medium(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t2Infiltrator.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.t2Infiltrator.getModifiedItemAttr(layer))

    def test_heavy(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.augmentedWasp.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.augmentedWasp.getModifiedItemAttr(layer))

    def test_sentry(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.imperialNavyCurator.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.imperialNavyCurator.getModifiedItemAttr(layer))

    def test_fighter(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.einherji.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            self.assertAlmostEquals(expected[layer], self.einherji.getModifiedItemAttr(layer))

    def test_fighterBomber(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.cyclops.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            self.assertAlmostEquals(expected[layer], self.cyclops.getModifiedItemAttr(layer))

    def test_electronicWarfare(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.sdHobgoblin.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.sdHobgoblin.getModifiedItemAttr(layer))

    def test_combatUtility(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.swBerserker.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.swBerserker.getModifiedItemAttr(layer))

    def test_logistic(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t2MediumArmorMaintenanceBot.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            expected.boost(layer, self.skill.getAttribute(layerBonus) * self.skillLevel)
            self.assertAlmostEquals(expected[layer], self.t2MediumArmorMaintenanceBot.getModifiedItemAttr(layer))

    def test_civilianMining(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.civilianMining.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            self.assertAlmostEquals(expected[layer], self.civilianMining.getModifiedItemAttr(layer))

    def test_mining(self):
        self.buildTested = 0
        expected = ModifiedAttributeDict()
        expected.original = self.t1Mining.item.attributes
        for layer, layerBonus in (("shieldCapacity", "shieldCapacityBonus"), ("armorHP", "armorHpBonus"), ("hp", "hullHpBonus")):
            self.assertAlmostEquals(expected[layer], self.t1Mining.getModifiedItemAttr(layer))
