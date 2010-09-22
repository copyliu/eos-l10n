from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Advanced Drone Interfacing"

    def tearDown(self):
        TestBase.tearDown(self)

    def test_maxGroupActive_droneControlUnit(self):
        self.buildTested = 0
        attr = "maxGroupActive"
        item = "Drone Control Unit I"
        iLvl = 1
        iIngame = 1
        fLvl = 4
        fIngame = 4
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
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
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
