from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Citadel Cruise Missiles"

    def test_emDamage_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Thunar Citadel Cruise Missile"
        cont = "Citadel Cruise Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Catastrophe Citadel Cruise Missile"
        cont = "Citadel Cruise Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Rajas Citadel Cruise Missile"
        cont = "Citadel Cruise Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Sol Citadel Cruise Missile"
        cont = "Citadel Cruise Launcher I"
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
        item = "Gremlin Rocket"
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

    def test_explosiveDamage_chargeOther(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Fulmination Assault Missile"
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

    def test_kineticDamage_chargeOther(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Juggernaut Torpedo"
        cont = "Siege Missile Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_chargeOther(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Flameburst Light Missile"
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
