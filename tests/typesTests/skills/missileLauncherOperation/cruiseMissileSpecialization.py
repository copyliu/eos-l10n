from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Cruise Missile Specialization"

    def test_speed_moduleWithSkillrq(self):
        self.buildTested = 0
        attr = "speed"
        item = "Cruise Missile Launcher II"
        iLvl = 1
        iIngame = 0.98
        fLvl = 4
        fIngame = 0.92
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_speed_moduleNoSkillrq(self):
        self.buildTested = 0
        attr = "speed"
        item = "Cruise Missile Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)