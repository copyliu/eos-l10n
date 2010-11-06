from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Silver Magnate"

    def test_amarrFrigate_capacitorNeed_moduleEnergyWeaponSmall(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Dual Light Beam Laser I"
        skill = "Amarr Frigate"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrFrigate_capacitorNeed_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Quad Light Beam Laser I"
        skill = "Amarr Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrFrigate_damageMultiplier_moduleEnergyWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Medium Beam Laser I"
        skill = "Amarr Frigate"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrFrigate_damageMultiplier_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Focused Medium Beam Laser I"
        skill = "Amarr Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
