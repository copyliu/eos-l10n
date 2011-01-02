from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Erebus"

    # Gallente Titan Skill Bonuses:
    # 100% bonus to Capital Hybrid Turret damage per level

    def test_gallenteTitan_damageMultiplier_moduleHybridWeaponCapital(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Ion Siege Blaster Cannon I"
        skill = "Gallente Titan"
        iLvl = 1
        iIngame = 2.0
        fLvl = 4
        fIngame = 5.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteTitan_damageMultiplier_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Electron Blaster Cannon I"
        skill = "Gallente Titan"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Titan Skill Bonuses:
    # 7.5% bonus to gang members' maximum armor HP per level

    def test_gallenteTitan_armorHP_fleetShip(self):
        self.buildTested = 0
        attr = "armorHP"
        skill = "Gallente Titan"
        iLvl = 1
        iIngame = 1.075
        fLvl = 4
        fIngame = 1.3
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship, gang=True)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Titan Skill Bonuses:
    # Can fit 1 additional Warfare Link module per level

    def test_gallenteTitan_maxGroupActive_moduleGangCoordinator(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Gallente Titan"
        item = "Information Warfare Link - Recon Operation"
        iLvl = 1
        iIngame = 2
        fLvl = 4
        fIngame = 5
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteTitan_maxGroupActive_moduleOther(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Gallente Titan"
        item = "100MN MicroWarpdrive I"
        iLvl = 1
        iIngame = 1
        fLvl = 4
        fIngame = 1
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Titan Skill Bonuses:
    # 99% reduction in CPU need for Warfare Link modules

    def test_static_cpu_moduleGangCoordinatorSkillrqLeadership(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Skirmish Warfare Link - Interdiction Maneuvers"
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
