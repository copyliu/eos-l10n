from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Orca"

    def test_industrialCommandShips_capacity_ship(self):
        self.buildTested = 0
        attr = "capacity"
        skill = "Industrial Command Ships"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_industrialCommandShips_commandBonus_moduleGangCoordinatorSkillrqMining(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Mining Foreman Link - Harvester Capacitor Efficiency"
        skill = "Industrial Command Ships"
        iLvl = 1
        iIngame = 1.03
        fLvl = 4
        fIngame = 1.12
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_industrialCommandShips_commandBonus_moduleGangCoordinatorSkillrqOther(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Armored Warfare Link - Damage Control"
        skill = "Industrial Command Ships"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxRange_moduleTractorBeam(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Small Tractor Beam I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 3.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxRange_moduleTractorBeamCapital(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Capital Tractor Beam I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 3.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxRange_moduleOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Salvager I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxTractorVelocity_moduleTractorBeam(self):
        self.buildTested = 0
        attr = "maxTractorVelocity"
        item = "Small Tractor Beam I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 2.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxTractorVelocity_moduleTractorBeamCapital(self):
        self.buildTested = 0
        attr = "maxTractorVelocity"
        item = "Capital Tractor Beam I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 2.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_surveyScanRange_moduleSurveyScanner(self):
        self.buildTested = 0
        attr = "surveyScanRange"
        item = "Survey Scanner I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 6.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
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

    def test_static_maxGroupActive_moduleGangCoordinator(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        item = "Siege Warfare Link - Shield Efficiency"
        ship_other = "Nighthawk"
        iIngame = 1.0
        fIngame = 3.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_maxGroupActive_moduleOther(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        item = "10MN Afterburner I"
        ship_other = "Nighthawk"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
