import unittest
from model import db
from model.types import Gang, Ship, Fit, Module, Skill, Character

class TestGang(unittest.TestCase):
    def setUp(self):
        self.g = Gang()
        self.g.leader = Fit()
        self.g.leader.ship = Ship(db.getItem("Rifter"))
        self.g.leader.character = Character("testety")

    def test_SkillGang(self):
        self.g.leader.character.getSkill("Leadership").level = 5
        self.g.calculateModifiedAttributes()
        new = self.g.leader.ship.getModifiedItemAttr("scanResolution")
        expected = self.g.leader.ship.item.getAttribute("scanResolution") * 1.1
        self.assertEquals(expected, new)

    def test_gangModGang(self):
        self.g.leader.modules.append(Module(db.getItem("Siege Warfare Link - Shield Harmonizing")))
        self.g.calculateModifiedAttributes()
        expected = self.g.leader.ship.item.getAttribute("shieldKineticDamageResonance") * 0.98
        new = self.g.leader.ship.getModifiedItemAttr("shieldKineticDamageResonance")
        self.assertEquals(expected, new)

    def test_ShipGang(self):
        self.g.leader.character.getSkill("Gallente Titan").level = 1
        self.g.leader.ship = Ship(db.getItem("Erebus"))
        self.g.calculateModifiedAttributes()
        new = self.g.leader.ship.getModifiedItemAttr("armorHP")
        expected = self.g.leader.ship.item.getAttribute("armorHP") * 1.075
        self.assertEquals(expected, new)