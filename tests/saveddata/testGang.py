import unittest
from eos import db
from eos.types import Gang, Wing, Squad, Ship, Fit, Module, Skill, Character

class TestGang(unittest.TestCase):
    def setUp(self):
        g = Gang()
        w = Wing()
        s = Squad()
        self.g = g
        self.s = s
        self.w = w
        g.wings.append(w)
        w.squads.append(s)
        f = Fit()
        self.s.members.append(f)
        self.s.members.append(Fit())
        self.s.leader = f
        f.ship = Ship(db.getItem("Rifter"))
        f.character = Character("testety")

    def test_SkillGang(self):
        self.s.leader.character.getSkill("Leadership").level = 5
        self.g.calculateModifiedAttributes()
        new = self.s.leader.ship.getModifiedItemAttr("scanResolution")
        expected = self.s.leader.ship.item.getAttribute("scanResolution") * 1.1
        self.assertEquals(expected, new)

    def test_gangModGang(self):
        self.s.leader.modules.append(Module(db.getItem("Siege Warfare Link - Shield Harmonizing")))
        self.g.calculateModifiedAttributes()
        expected = self.s.leader.ship.item.getAttribute("shieldKineticDamageResonance") * 0.98
        new = self.s.leader.ship.getModifiedItemAttr("shieldKineticDamageResonance")
        self.assertEquals(expected, new)

    def test_ShipGang(self):
        self.s.leader.character.getSkill("Gallente Titan").level = 1
        self.s.leader.ship = Ship(db.getItem("Erebus"))
        self.g.calculateModifiedAttributes()
        new = self.s.leader.ship.getModifiedItemAttr("armorHP")
        expected = self.s.leader.ship.item.getAttribute("armorHP") * 1.075
        self.assertEquals(expected, new)

    def test_onlyFC(self):
        self.g.leader = Fit()
        self.g.leader.ship = Ship(db.getItem("Rifter"))
        self.g.leader.character = Character("tootoot")
        self.g.leader.character.getSkill("Leadership").level = 5
        self.s.leader.character.getSkill("Leadership").level = 5
        self.g.calculateModifiedAttributes()
        self.assertEquals(self.g.leader.ship.item.getAttribute("scanResolution"), self.g.leader.ship.getModifiedItemAttr("scanResolution"))
        self.assertEquals(self.s.leader.ship.item.getAttribute("scanResolution") * 1.1, self.s.leader.ship.getModifiedItemAttr("scanResolution"))

    def test_onlyWC(self):
        self.w.leader = Fit()
        self.w.leader.ship = Ship(db.getItem("Rifter"))
        self.w.leader.character = Character("tootoot")
        self.w.leader.character.getSkill("Leadership").level = 5
        self.s.leader.character.getSkill("Leadership").level = 5
        self.g.calculateModifiedAttributes()
        self.assertEquals(self.s.leader.ship.item.getAttribute("scanResolution") * 1.1, self.s.leader.ship.getModifiedItemAttr("scanResolution"))
        self.assertEquals(self.w.leader.ship.item.getAttribute("scanResolution") * 1.1, self.w.leader.ship.getModifiedItemAttr("scanResolution"))