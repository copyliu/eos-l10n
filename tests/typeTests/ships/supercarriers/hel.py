from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Hel"

    def test_minmatarCarrier_shieldTransferRange_moduleShieldTransporterCapital(self):
        self.buildTested = 0
        attr = "shieldTransferRange"
        item = "Capital Shield Transporter I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.5
        fLvl = 4
        fIngame = 3.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_shieldTransferRange_moduleShieldTransporterOther(self):
        self.buildTested = 0
        attr = "shieldTransferRange"
        item = "Medium Shield Transporter I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_maxRange_moduleRemoteRepairerCapital(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Capital Remote Armor Repair System I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.5
        fLvl = 4
        fIngame = 3.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_maxRange_moduleRemoteRepairerOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Small Remote Armor Repair System I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_shieldBonus_moduleShieldTransporterCapital(self):
        self.buildTested = 0
        attr = "shieldBonus"
        item = "Capital Shield Transporter I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_shieldBonus_moduleShieldTransporter(self):
        self.buildTested = 0
        attr = "shieldBonus"
        item = "Medium Shield Transporter I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_shieldBonus_moduleShieldTransporterCivilian(self):
        self.buildTested = 0
        attr = "shieldBonus"
        item = "Civilian Remote Shield Transporter"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_shieldBonus_moduleOther(self):
        self.buildTested = 0
        attr = "shieldBonus"
        item = "X-Large Shield Booster I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_armorDamageAmount_moduleRemoteArmorRepairerCapital(self):
        self.buildTested = 0
        attr = "armorDamageAmount"
        item = "Capital Remote Armor Repair System I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_armorDamageAmount_moduleRemoteArmorRepairer(self):
        self.buildTested = 0
        attr = "armorDamageAmount"
        item = "Small Remote Armor Repair System I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_armorDamageAmount_moduleRemoteArmorRepairerCivilian(self):
        self.buildTested = 0
        attr = "armorDamageAmount"
        item = "Civilian Remote Armor Repair System"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_armorDamageAmount_moduleOther(self):
        self.buildTested = 0
        attr = "armorDamageAmount"
        item = "Small Armor Repairer I"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_maxActiveDrones_ship(self):
        self.buildTested = 0
        attr = "maxActiveDrones"
        skill = "Minmatar Carrier"
        iLvl = 1
        iIngame = 8.0
        fLvl = 4
        fIngame = 17.0
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_maxGroupActive_moduleGangCoordinator(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Minmatar Carrier"
        item = "Siege Warfare Link - Shield Harmonizing"
        iLvl = 1
        iIngame = 2
        fLvl = 4
        fIngame = 5
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarCarrier_maxGroupActive_moduleOther(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        skill = "Minmatar Carrier"
        item = "Remote ECM Burst I"
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
        item = "Information Warfare Link - Electronic Superiority"
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

    def test_static_cpu_moduleDroneControlUnit(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Drone Control Unit I"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 0.01
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_droneControlRange_ship(self):
        self.buildTested = 0
        attr = "droneControlRange"
        ship_other = "Abaddon"
        iIngame = 1.0
        fIngame = 3.0
        iEos = self.getShipAttr(attr, ship=ship_other)
        fEos = self.getShipAttr(attr, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)