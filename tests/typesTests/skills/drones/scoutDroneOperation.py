from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Scout Drone Operation"

    def test_droneControlRange(self):
        self.buildTested = 0
        attr = "droneControlRange"
        iLvl = 1
        iIngame = 5000
        fLvl = 4
        fIngame = 20000
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
