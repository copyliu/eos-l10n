from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Velator"

    # Special Ability:
    # 5% bonus to hybrid turret damage per skill level
    # Description is wrong, it uses Gallente Frigate as boost skill

    def test_gallenteFrigate_damageMultiplier_moduleHybridWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Light Ion Blaster I"
        skill = "Gallente Frigate"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteFrigate_damageMultiplier_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "200mm Railgun I"
        skill = "Gallente Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
