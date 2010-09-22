from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Fighters"

    def tearDown(self):
        TestBase.tearDown(self)

    def test_damageMultiplier_droneFighter(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Templar"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_damageMultiplier_droneOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Praetor II"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
