from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Tactical Logistics Reconfiguration"

    def test_consumptionQuantity_moduleSiegeModuleSkillrq(self):
        self.buildTested = 0
        attr = "consumptionQuantity"
        item = "Triage Module I"
        iLvl = 1
        iIngame = 225
        fLvl = 4
        fIngame = 150
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_consumptionQuantity_moduleSiegeModuleNoSkillrq(self):
        self.buildTested = 0
        attr = "consumptionQuantity"
        item = "Industrial Core I"
        iLvl = 1
        iIngame = 500
        fLvl = 4
        fIngame = 500
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_consumptionQuantity_moduleOther(self):
        self.buildTested = 0
        attr = "consumptionQuantity"
        item = "Covert Cynosural Field Generator I"
        iLvl = 1
        iIngame = 500
        fLvl = 4
        fIngame = 500
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)