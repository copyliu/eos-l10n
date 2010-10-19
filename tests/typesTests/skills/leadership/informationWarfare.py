from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Information Warfare"

    def test_maxTargetRange_fleetShip(self):
        self.buildTested = 0
        attr = "maxTargetRange"
        iLvl = 1
        iIngame = 1.02
        fLvl = 4
        fIngame = 1.08
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, gang=True)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_maxTargetRange_fleetSubsystem(self):
        self.buildTested = 0
        attr = "maxTargetRange"
        item = "Loki Electronics - Emergent Locus Analyzer"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, gang=True)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
