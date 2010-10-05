from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Citadel Torpedoes"

    def test_emDamage_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Thor Citadel Torpedo"
        cont = "Citadel Torpedo Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamage_chargeOther(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Sabretooth Light Missile"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Doom Citadel Torpedo"
        cont = "Citadel Torpedo Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_chargeOther(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Phalanx Rocket"
        cont = "Rocket Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Rift Citadel Torpedo"
        cont = "Citadel Torpedo Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_chargeOther(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Terror Assault Missile"
        cont = "Heavy Assault Missile Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Purgatory Citadel Torpedo"
        cont = "Citadel Torpedo Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_chargeOther(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Widowmaker Heavy Missile"
        cont = "Heavy Missile Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
