from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Signal Suppression"
        self.attrs = ("maxTargetRangeBonus", "scanResolutionBonus")

    def test_sensorDamp_moduleRemoteSensorDamper(self):
        self.buildTested = 0
        item = "Remote Sensor Dampener I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        for attr in self.attrs:
            iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
            fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
            dIngame = fIngame / iIngame
            dEos = fEos / iEos
            self.assertAlmostEquals(dEos, dIngame)

    def test_sensorDamp_moduleOtherSkillrqSenslink(self):
        self.buildTested = 0
        attrs = ("maxTargetRangeBonus", "scanResolutionBonus")
        item = "Remote Sensor Booster I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        for attr in self.attrs:
            iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
            fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
            dIngame = fIngame / iIngame
            dEos = fEos / iEos
            self.assertAlmostEquals(dEos, dIngame)
