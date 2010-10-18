from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Armored Warfare Specialist"

    def test_commandBonus_moduleGangCoordinatorSkillrq(self):
        self.buildTested = 0
        attr = "commandBonus"
        item = "Armored Warfare Link - Passive Defense"
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
        item = "Mining Foreman Link - Harvester Capacitor Efficiency"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
