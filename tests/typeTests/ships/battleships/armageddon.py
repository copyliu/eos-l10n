from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Armageddon"

    def test_amarrBattleship_capacitorNeed_moduleEnergyWeaponLarge(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Mega Beam Laser I"
        skill = "Amarr Battleship"
        iLvl = 1
        iIngame = 0.9
        fLvl = 4
        fIngame = 0.6
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrBattleship_capacitorNeed_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Quad Light Beam Laser I"
        skill = "Amarr Battleship"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrBattleship_speed_moduleEnergyWeaponLarge(self):
        self.buildTested = 0
        attr = "speed"
        item = "Tachyon Beam Laser I"
        skill = "Amarr Battleship"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrBattleship_speed_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "speed"
        item = "Heavy Pulse Laser I"
        skill = "Amarr Battleship"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
