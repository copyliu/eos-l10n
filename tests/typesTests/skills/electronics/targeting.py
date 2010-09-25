from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Targeting"

    def test_maxTargetsLockedFromSkills(self):
        self.buildTested = 0
        attr = "maxTargetsLockedFromSkills"
        iLvl = 1
        iIngame = 1
        fLvl = 4
        fIngame = 4
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
