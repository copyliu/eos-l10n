from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Turret Destabilization"

    def test_turretDisruption_moduleTrackingDisruptor(self):
        self.buildTested = 0
        attrs = ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus")
        item = "Tracking Disruptor I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        for attr in attrs:
            iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
            fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
            dIngame = fIngame / iIngame
            dEos = fEos / iEos
            self.assertAlmostEquals(dEos, dIngame)

    def test_turretDisruption_moduleOther(self):
        self.buildTested = 0
        attrs = ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus")
        item = "Tracking Link I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        for attr in attrs:
            iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
            fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
            dIngame = fIngame / iIngame
            dEos = fEos / iEos
            self.assertAlmostEquals(dEos, dIngame)
