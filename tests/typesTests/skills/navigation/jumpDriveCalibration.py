from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Jump Drive Calibration"

    def test_jumpDriveRange_ship(self):
        self.buildTested = 0
        attr = "jumpDriveRange"
        ship = "Archon"
        iLvl = 1
        iIngame = 1.25
        fLvl = 4
        fIngame = 2.0
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, ship=ship)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
