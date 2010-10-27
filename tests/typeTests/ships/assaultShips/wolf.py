from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Wolf"

    def test_minmatarFrigate_damageMultiplier_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "200mm AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_damageMultiplier_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "425mm AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_assaultShips_damageMultiplier_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "280mm Howitzer Artillery I"
        skill = "Assault Ships"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_assaultShips_damageMultiplier_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "650mm Artillery Cannon I"
        skill = "Assault Ships"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_assaultShips_falloff_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "falloff"
        item = "150mm Light AutoCannon I"
        skill = "Assault Ships"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_assaultShips_falloff_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "falloff"
        item = "220mm Vulcan AutoCannon I"
        skill = "Assault Ships"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
