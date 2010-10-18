from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Archaeology"

    def test_accessDifficultyBonus_moduleDataMinerSkillrq(self):
        self.buildTested = 0
        attr = "accessDifficultyBonus"
        item = "Analyzer I"
        iLvl = 1
        iIngame = 10.0
        fLvl = 4
        fIngame = 25.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_accessDifficultyBonus_moduleDataMinerNoSkillrq(self):
        self.buildTested = 0
        attr = "accessDifficultyBonus"
        item = "Codebreaker I"
        iLvl = 1
        iIngame = 5.0
        fLvl = 4
        fIngame = 5.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
