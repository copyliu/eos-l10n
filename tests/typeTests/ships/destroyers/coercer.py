from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Coercer"

    def test_destroyers_trackingSpeed_moduleEnergyWeaponSmall(self):
        self.buildTested = 0
        attr = "trackingSpeed"
        item = "Gatling Pulse Laser I"
        skill = "Destroyers"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_destroyers_trackingSpeed_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "trackingSpeed"
        item = "Quad Light Beam Laser I"
        skill = "Destroyers"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_destroyers_capacitorNeed_moduleEnergyWeaponSmall(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Dual Light Beam Laser I"
        skill = "Destroyers"
        iLvl = 1
        iIngame = 0.9
        fLvl = 4
        fIngame = 0.6
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_destroyers_capacitorNeed_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Heavy Pulse Laser I"
        skill = "Destroyers"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_speed_moduleEnergyWeapon(self):
        self.buildTested = 0
        attr = "speed"
        item = "Dual Light Pulse Laser I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.25
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_speed_moduleHybridWeapon(self):
        self.buildTested = 0
        attr = "speed"
        item = "250mm Railgun I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.25
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_speed_moduleProjectileWeapon(self):
        self.buildTested = 0
        attr = "speed"
        item = "150mm Light AutoCannon I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.25
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_speed_moduleOther(self):
        self.buildTested = 0
        attr = "speed"
        item = "Core Probe Launcher I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxRange_moduleEnergyWeaponSmall(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Medium Pulse Laser I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxRange_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Heavy Beam Laser I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
