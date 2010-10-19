from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Skirmish Warfare"

    def test_agility_fleetShip(self):
        self.buildTested = 0
        attr = "agility"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, gang=True)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_fleetSubsystem(self):
        self.buildTested = 0
        attr = "agility"
        item = "Tengu Propulsion - Gravitational Capacitor"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, gang=True)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
