from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Signature Analysis"

    # 5% improved targeting speed per skill level.

    def test_scanResolution_ship(self):
        self.buildTested = 0
        attr = "scanResolution"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl))
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl))
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
