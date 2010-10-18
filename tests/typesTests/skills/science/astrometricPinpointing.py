from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Astrometric Pinpointing"

    def test_baseMaxScanDeviation_chargeScanProbe(self):
        self.buildTested = 0
        attr = "baseMaxScanDeviation"
        item = "Core Scanner Probe I"
        iLvl = 1
        iIngame = 0.9
        fLvl = 4
        fIngame = 0.6
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
