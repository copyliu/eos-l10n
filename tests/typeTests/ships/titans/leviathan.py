from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Leviathan"

    def test_caldariTitan_kineticDamage_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Rift Citadel Torpedo"
        skill = "Caldari Titan"
        iLvl = 1
        iIngame = 2.25
        fLvl = 4
        fIngame = 6.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariTitan_kineticDamage_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Rajas Citadel Cruise Missile"
        skill = "Caldari Titan"
        iLvl = 1
        iIngame = 2.25
        fLvl = 4
        fIngame = 6.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariTitan_kineticDamage_chargeMissileOther(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Bloodclaw Light Missile"
        skill = "Caldari Titan"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariTitan_shieldCapacity_fleetShip(self):
        self.buildTested = 0
        attr = "shieldCapacity"
        skill = "Caldari Titan"
        iLvl = 1
        iIngame = 1.075
        fLvl = 4
        fIngame = 1.3
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship, gang=True)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariTitan_maxGroupActive_moduleGangCoordinator(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Caldari Titan"
        item = "Siege Warfare Link - Shield Efficiency"
        iLvl = 1
        iIngame = 2
        fLvl = 4
        fIngame = 5
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariTitan_maxGroupActive_moduleOther(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Caldari Titan"
        item = "1MN Afterburner I"
        iLvl = 1
        iIngame = 1
        fLvl = 4
        fIngame = 1
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_cpu_moduleGangCoordinatorSkillrqLeadership(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Armored Warfare Link - Damage Control"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 0.01
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_cpu_moduleGangCoordinatorNoSkillrqLeadership(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Command Processor I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
