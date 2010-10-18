from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Jump Drive Operation"

    def test_jumpDriveCapacitorNeed_ship(self):
        self.buildTested = 0
        attr = "jumpDriveCapacitorNeed"
        ship = "Revelation"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, ship=ship)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
