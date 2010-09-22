from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Fighter Bombers"

    def tearDown(self):
        TestBase.tearDown(self)

    def test_emDamage_droneFighterBomber(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Malleus"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, getCharge=True)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, getCharge=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_droneFighterBomber(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Tyrfing"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, getCharge=True)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, getCharge=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_droneFighterBomber(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Mantis"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, getCharge=True)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, getCharge=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_droneFighterBomber(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Cyclops"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, getCharge=True)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, getCharge=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamage_other(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Mjolnir Torpedo"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont="Siege Missile Launcher II")
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont="Siege Missile Launcher II")
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_other(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Bane Torpedo"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont="Siege Missile Launcher II")
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont="Siege Missile Launcher II")
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_other(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Juggernaut Torpedo"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont="Siege Missile Launcher II")
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont="Siege Missile Launcher II")
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_other(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Inferno Torpedo"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont="Siege Missile Launcher II")
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont="Siege Missile Launcher II")
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
