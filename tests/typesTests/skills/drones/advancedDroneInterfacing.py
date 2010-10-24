from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Advanced Drone Interfacing"

    def test_maxGroupActive_moduleDroneControlUnit(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        item = "Drone Control Unit I"
        iLvl = 1
        iIngame = 1
        fLvl = 4
        fIngame = 4
        iEos = self.testItemAttr(attr, item, skill=(self.skill, iLvl))
        fEos = self.testItemAttr(attr, item, skill=(self.skill, fLvl))
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_maxGroupActive_moduleOther(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        item = "Gas Cloud Harvester I"
        iLvl = 1
        iIngame = 0
        fLvl = 4
        fIngame = 0
        iEos = self.testItemAttr(attr, item, skill=(self.skill, iLvl))
        fEos = self.testItemAttr(attr, item, skill=(self.skill, fLvl))
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
