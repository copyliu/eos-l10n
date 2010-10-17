from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Cloning Facility Operation"

    def test_maxJumpClones_shipTitan(self):
        self.buildTested = 0
        attr = "maxJumpClones"
        ship = "Erebus"
        iLvl = 1
        iIngame = 1.15
        fLvl = 4
        fIngame = 1.6
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, ship=ship)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_maxJumpClones_shipCapitalIndustrial(self):
        self.buildTested = 0
        attr = "maxJumpClones"
        ship = "Rorqual"
        iLvl = 1
        iIngame = 1.15
        fLvl = 4
        fIngame = 1.6
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, ship=ship)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
