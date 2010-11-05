from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Cheetah"

    def test_minmatarFrigate_damageMultiplier_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "200mm AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_damageMultiplier_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Dual 180mm AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_maxRange_moduleProjectileWeaponSmall(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "280mm Howitzer Artillery I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_maxRange_moduleProjectileWeaponOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "650mm Artillery Cannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_covertOps_cpu_moduleCloakingDevice(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Prototype Cloaking Device I"
        skill = "Covert Ops"
        iLvl = 1
        iIngame = 0.02
        fLvl = 4
        fIngame = 0.005
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_covertOps_cpu_moduleOther(self):
        self.buildTested = 0
        attr = "cpu"
        item = "Gyrostabilizer I"
        skill = "Covert Ops"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_covertOps_baseSensorStrength_chargeScannerProbe(self):
        self.buildTested = 0
        attr = "baseSensorStrength"
        item = "Core Scanner Probe I"
        skill = "Covert Ops"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_covertOps_explosionDelay_chargeSurveyProbe(self):
        self.buildTested = 0
        attr = "explosionDelay"
        item = "Discovery Survey Probe I"
        skill = "Covert Ops"
        iLvl = 1
        iIngame = 0.9
        fLvl = 4
        fIngame = 0.6
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_covertOps_explosionDelay_chargeOther(self):
        self.buildTested = 0
        attr = "explosionDelay"
        item = "Combat Scanner Probe I"
        skill = "Covert Ops"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_moduleReactivationDelay_moduleCloakingDevice(self):
        self.buildTested = 0
        attr = "moduleReactivationDelay"
        item = "Prototype Cloaking Device I"
        ingame = 5000.0
        eos = self.getItemAttr(attr, item, ship=self.ship)
        self.assertAlmostEquals(eos, ingame)

    def test_static_moduleReactivationDelay_moduleOther(self):
        self.buildTested = 0
        attr = "moduleReactivationDelay"
        iItem = "Prototype Cloaking Device I"
        iIngame = 5000.0
        fItem = "Covert Cynosural Field Generator I"
        fIngame = 30000.0
        iEos = self.getItemAttr(attr, iItem, ship=self.ship)
        fEos = self.getItemAttr(attr, fItem, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
