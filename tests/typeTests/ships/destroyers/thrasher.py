from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Thrasher"

    def test_destroyers_trackingSpeed_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "trackingSpeed"
        item = "125mm Gatling AutoCannon I"
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

    def test_destroyers_trackingSpeed_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "trackingSpeed"
        item = "425mm AutoCannon I"
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

    def test_destroyers_damageMultiplier_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "280mm Howitzer Artillery I"
        skill = "Destroyers"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_destroyers_damageMultiplier_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Dual 180mm AutoCannon I"
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
        item = "Heavy Pulse Laser I"
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
        item = "Ion Blaster Cannon I"
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
        item = "650mm Artillery Cannon I"
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

    def test_static_maxRange_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "150mm Light AutoCannon I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxRange_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "220mm Vulcan AutoCannon I"
        ship_other = "Punisher"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
