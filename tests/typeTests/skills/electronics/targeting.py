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
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl))
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl))
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
