from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Phoenix"

    def test_caldariDreadnought_kineticDamage_chargeMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Rift Citadel Torpedo"
        skill = "Caldari Dreadnought"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariDreadnought_kineticDamage_chargeMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Rajas Citadel Cruise Missile"
        skill = "Caldari Dreadnought"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariDreadnought_kineticDamage_chargeMissileOther(self):
        self.buildTested = 0
        attr = "kineticDamage"
        item = "Juggernaut Torpedo"
        skill = "Caldari Dreadnought"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariDreadnought_speed_moduleLauncherMissileCitadelTorpedo(self):
        self.buildTested = 0
        attr = "speed"
        item = "Citadel Torpedo Launcher I"
        skill = "Caldari Dreadnought"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariDreadnought_speed_moduleLauncherMissileCitadelCruise(self):
        self.buildTested = 0
        attr = "speed"
        item = "Citadel Cruise Launcher I"
        skill = "Caldari Dreadnought"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariDreadnought_speed_moduleLauncherMissileOther(self):
        self.buildTested = 0
        attr = "speed"
        item = "Assault Missile Launcher I"
        skill = "Caldari Dreadnought"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)