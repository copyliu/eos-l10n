import unittest
from model import db
from model.types import Fit, DamagePattern, Ship, Module, State

class TestDamagePattern(unittest.TestCase):
    def test_rawEhp(self):
        f = Fit()
        f.ship = Ship(db.getItem("Wolf"))
        expected = 0
        for type in ("shieldCapacity", "armorHP", "hp"):
            expected += f.ship.getModifiedItemAttr(type)

        self.assertEquals(expected, sum(f.getEhp().values()))

    def test_uniformEhp(self):
        f = Fit()
        f.ship = Ship(db.getItem("Wolf"))
        f.damagePattern = DamagePattern(25, 25, 25 ,25)
        self.assertAlmostEquals(3094, sum(f.getEhp().values()), 0)

    def test_passiveRechargeUniform(self):
        f = Fit()
        f.ship = Ship(db.getItem("Wolf"))
        f.damagePattern = DamagePattern(25, 25, 25 ,25)
        self.assertAlmostEquals(3.8, f.getEffectiveTank()["passiveShield"], 1)

    def test_armorRepairUniform(self):
        f = Fit()
        f.ship = Ship(db.getItem("Wolf"))
        f.damagePattern = DamagePattern(25, 25, 25 ,25)
        m = Module(db.getItem("Small Armor Repairer I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        f.calculateModifiedAttributes()
        self.assertAlmostEquals(19.3, f.getEffectiveTank()["armor"],1)

    def test_shieldBoostUniform(self):
        f = Fit()
        f.ship = Ship(db.getItem("Wolf"))
        f.damagePattern = DamagePattern(25, 25, 25 ,25)
        m = Module(db.getItem("Small Shield Booster I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        f.calculateModifiedAttributes()
        self.assertAlmostEquals(26.3, f.getEffectiveTank()["shield"],1)

    def test_hullRepairUniform(self):
        f = Fit()
        f.ship = Ship(db.getItem("Wolf"))
        f.damagePattern = DamagePattern(25, 25, 25 ,25)
        m = Module(db.getItem("Small Hull Repairer I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        f.calculateModifiedAttributes()
        self.assertAlmostEquals(f.extraAttributes["hullRepair"], f.getEffectiveTank()["hull"],1)