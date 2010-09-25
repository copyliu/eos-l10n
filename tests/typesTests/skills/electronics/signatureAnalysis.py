from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Signature Analysis"

    def test_scanResolution_ship(self):
        self.buildTested = 0
        attr = "scanResolution"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_scanResolution_subsystem(self):
        self.buildTested = 0
        attr = "scanResolution"
        item = "Tengu Electronics - Dissolution Sequencer"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
