from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Jump Portal Generation"

    def test_consumptionQuantity_moduleJumpPortalGenerator(self):
        self.buildTested = 0
        attr = "consumptionQuantity"
        item = "Jump Portal Generator I"
        iLvl = 1
        iIngame = 450.0
        fLvl = 4
        fIngame = 300.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_consumptionQuantity_moduleOther(self):
        self.buildTested = 0
        attr = "consumptionQuantity"
        item = "Cynosural Field Generator I"
        iLvl = 1
        iIngame = 500.0
        fLvl = 4
        fIngame = 500.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
