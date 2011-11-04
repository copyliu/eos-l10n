from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Naga"

    # Battlecruiser Skill Bonus Per Level:
    # 10% bonus to Torpedo Velocity

    def test_battlecruisers_maxVelocity_chargeMissileTorpedo(self):
        self.buildTested = 0
        attr = "maxVelocity"
        item = "Bane Torpedo"
        skill = "Battlecruisers"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_battlecruisers_maxVelocity_chargeMissileTorpedoAdvanced(self):
        self.buildTested = 0
        attr = "maxVelocity"
        item = "Juggernaut Rage Torpedo"
        skill = "Battlecruisers"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_battlecruisers_maxVelocity_chargeMissileOther(self):
        self.buildTested = 0
        attr = "maxVelocity"
        item = "Paradise Cruise Missile"
        skill = "Battlecruisers"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Battlecruiser Skill Bonus Per Level:
    # 10% bonus to Large Hybrid Turret optimal range

    def test_battlecruisers_maxRange_moduleHybridWeaponLarge(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "425mm Railgun I"
        skill = "Battlecruisers"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_battlecruisers_maxRange_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "200mm Railgun I"
        skill = "Battlecruisers"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Role Bonus:
    # 95% reduction in the powergrid need of Large Hybrid Turrets

    def test_static_power_moduleHybridWeaponLarge(self):
        self.buildTested = 0
        attr = "power"
        item = "Ion Blaster Cannon I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 0.05
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_power_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "power"
        item = "Dual 150mm Railgun I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Role Bonus:
    # 50% reduction in the CPU need of Large Hybrid Turrets

    def test_static_cpu_moduleHybridWeaponLarge(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Neutron Blaster Cannon I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 0.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_cpu_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Light Electron Blaster I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Role Bonus:
    # 50% reduction in the capacitor need of Large Hybrid Turrets

    def test_static_capacitorNeed_moduleHybridWeaponLarge(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Dual 250mm Railgun I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 0.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_capacitorNeed_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Heavy Ion Blaster I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Role Bonus:
    # 40% reduction in the powergrid need of Siege Missile Launchers
    # Actually it's 94%, mistype in description

    def test_static_power_moduleLauncherMissileSiege(self):
        self.buildTested = 0
        attr = "power"
        item = "Siege Missile Launcher I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 0.06
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_power_moduleLauncherMissileOther(self):
        self.buildTested = 0
        attr = "power"
        item = "Rocket Launcher I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Role Bonus:
    # 58% reduction in the CPU need of Siege Missile Launchers

    def test_static_cpu_moduleLauncherMissileSiege(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Siege Missile Launcher I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 0.42
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_cpu_moduleLauncherMissileOther(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Cruise Missile Launcher I"
        ship_other = "Raven"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
