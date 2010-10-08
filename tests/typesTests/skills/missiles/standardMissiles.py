from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Standard Missiles"

    def test_emDamage_chargeMissileLight(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Sabretooth Light Missile"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamage_chargeMissileLightAdvanced(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Sabretooth Fury Light Missile"
        cont = "Standard Missile Launcher II"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamage_chargeMissileLightFof(self):
        self.buildTested = 0
        attr = "emDamage"
        item = "Seeker F.O.F. Light Missile I"
        cont = "Standard Missile Launcher I"
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

    def test_explosiveDamage_chargeMissileLight(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Piranha Light Missile"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_chargeMissileLightAdvanced(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Piranha Precision Light Missile"
        cont = "Standard Missile Launcher II"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_explosiveDamage_chargeMissileLightFof(self):
        self.buildTested = 0
        attr = "explosiveDamage"
        item = "Exterminator F.O.F. Light Missile I"
        cont = "Standard Missile Launcher I"
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
        item = "Havoc Heavy Missile"
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

    def test_kineticDamage_chargeMissileLight(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Bloodclaw Light Missile"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_chargeMissileLightAdvanced(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Bloodclaw Fury Light Missile"
        cont = "Standard Missile Launcher II"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_chargeMissileLightFof(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Serpent F.O.F. Light Missile I"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_kineticDamage_chargeMissileLightNoSkillrqMissileOp(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Civilian Bloodclaw Light Missile"
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

    def test_thermalDamage_chargeMissileLight(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Flameburst Light Missile"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_chargeMissileLightAdvanced(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Flameburst Fury Light Missile"
        cont = "Standard Missile Launcher II"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_thermalDamage_chargeMissileLightFof(self):
        self.buildTested = 0
        attr = "thermalDamage"
        item = "Firefly F.O.F. Light Missile I"
        cont = "Standard Missile Launcher I"
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
        item = "Sol Citadel Cruise Missile"
        cont = "Citadel Cruise Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
