from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Capital Repair Systems"

    def test_duration_moduleArmorRepairerSkillrq(self):
        self.buildTested = 0
        attr = "duration"
        item = "Capital Armor Repairer I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_duration_moduleArmorRepairerNoSkillrq(self):
        self.buildTested = 0
        attr = "duration"
        item = "Medium Armor Repairer I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
