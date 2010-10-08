from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Target Navigation Prediction"

    def test_aoeVelocity_chargeMissileRocket(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Gremlin Rocket"
        cont = "Rocket Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileRocketAdvanced(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Phalanx Javelin Rocket"
        cont = "Rocket Launcher II"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileLight(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Bloodclaw Light Missile"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileLightNoSkillrqMissileOp(self):
        self.buildTested = 0
        attr = "aoeVelocity"
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

    def test_aoeVelocity_chargeMissileLightAdvanced(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Piranha Fury Light Missile"
        cont = "Standard Missile Launcher II"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileLightFof(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Seeker F.O.F. Light Missile I"
        cont = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileAssault(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Hellfire Assault Missile"
        cont = "Heavy Assault Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileAssaultAdvanced(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Fulmination Rage Assault Missile"
        cont = "Heavy Assault Missile Launcher II"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileHeavy(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Havoc Heavy Missile"
        cont = "Heavy Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileHeavyAdvanced(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Scourge Precision Heavy Missile"
        cont = "Heavy Missile Launcher II"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileHeavyFof(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Hydra F.O.F. Heavy Missile I"
        cont = "Heavy Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileTorpedo(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Bane Torpedo"
        cont = "Siege Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileTorpedoAdvanced(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Juggernaut Rage Torpedo"
        cont = "Siege Missile Launcher II"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileCruise(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Paradise Cruise Missile"
        cont = "Cruise Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileCruiseAdvanced(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Paradise Fury Cruise Missile"
        cont = "Cruise Missile Launcher II"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileCruiseFof(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Phoenix F.O.F. Cruise Missile I"
        cont = "Cruise Missile Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Purgatory Citadel Torpedo"
        cont = "Citadel Torpedo Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_aoeVelocity_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "aoeVelocity"
        item = "Catastrophe Citadel Cruise Missile"
        cont = "Citadel Cruise Launcher I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
