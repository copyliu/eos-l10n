from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Astrometric Rangefinding"

    def test_baseSensorStrength_chargeScanProbe(self):
        self.buildTested = 0
        attr = "baseSensorStrength"
        item = "Combat Scanner Probe I"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
