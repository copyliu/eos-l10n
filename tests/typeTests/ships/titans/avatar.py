from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Avatar"

    def test_amarrTitan_damageMultiplier_moduleEnergyWeaponCapital(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Dual Giga Pulse Laser I"
        skill = "Amarr Titan"
        iLvl = 1
        iIngame = 2.0
        fLvl = 4
        fIngame = 5.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrTitan_damageMultiplier_moduleEnergyWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Medium Pulse Laser I"
        skill = "Amarr Titan"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrTitan_rechargeRate_fleetShip(self):
        self.buildTested = 0
        attr = "rechargeRate"
        skill = "Amarr Titan"
        iLvl = 1
        iIngame = 0.925
        fLvl = 4
        fIngame = 0.7
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship, gang=True)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrTitan_maxGroupActive_moduleGangCoordinator(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Amarr Titan"
        item = "Armored Warfare Link - Passive Defense"
        iLvl = 1
        iIngame = 2
        fLvl = 4
        fIngame = 5
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrTitan_maxGroupActive_moduleOther(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Amarr Titan"
        item = "ECM Burst I"
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
        item = "Information Warfare Link - Recon Operation"
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
