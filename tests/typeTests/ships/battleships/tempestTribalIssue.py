from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Tempest Tribal Issue"

    # Minmatar Battleship Skill Bonus:
    # 5% bonus to Large Projectile Turret rate of fire per level

    def test_minmatarBattleship_speed_moduleProjectileWeaponLarge(self):
        self.buildTested = 0
        attr = "speed"
        item = "1200mm Artillery Cannon I"
        skill = "Minmatar Battleship"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarBattleship_speed_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "speed"
        item = "150mm Light AutoCannon I"
        skill = "Minmatar Battleship"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Minmatar Battleship Skill Bonus:
    # 5% bonus to Large Projectile Turret damage per level

    def test_minmatarBattleship_damageMultiplier_moduleProjectileWeaponLarge(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Dual 425mm AutoCannon I"
        skill = "Minmatar Battleship"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarBattleship_damageMultiplier_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "425mm AutoCannon I"
        skill = "Minmatar Battleship"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
