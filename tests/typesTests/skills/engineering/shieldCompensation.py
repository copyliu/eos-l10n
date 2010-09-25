from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Shield Compensation"

    def test_capacitorNeed_moduleShieldBoosterSkillrqShieldOperation(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Large Shield Booster I"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_capacitorNeed_moduleShieldBoosterSkillrqCapitalShieldOperation(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Capital Shield Booster I"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_capacitorNeed_moduleShieldBoosterSkillrqNone(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Civilian Shield Booster I"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_capacitorNeed_moduleOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Medium Proton Smartbomb I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
