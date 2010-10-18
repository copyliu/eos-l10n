from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Mining Director"

    def test_commandBonus_moduleGangCoordinatorSkillrq(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Mining Foreman Link - Mining Laser Field Enhancement"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 4.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_commandBonus_moduleGangCoordinatorNoSkillrq(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Information Warfare Link - Recon Operation"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
