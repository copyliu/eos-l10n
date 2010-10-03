from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Gunnery"

    def test_speed_moduleEnergyWeapon(self):
        self.buildTested = 0
        attr = "speed"
        item = "Dual Light Beam Laser I"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_speed_moduleHybridWeapon(self):
        self.buildTested = 0
        attr = "speed"
        item = "Dual 150mm Railgun I"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_speed_moduleProjectileWeapon(self):
        self.buildTested = 0
        attr = "speed"
        item = "150mm Light AutoCannon I"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_speed_moduleOther(self):
        self.buildTested = 0
        attr = "speed"
        item = "Rocket Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
