from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Biology"

    def test_boosterDuration_booster(self):
        self.buildTested = 0
        attr = "boosterDuration"
        item = "Synth Crash Booster"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
