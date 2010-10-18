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
