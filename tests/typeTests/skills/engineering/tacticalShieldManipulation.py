from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Tactical Shield Manipulation"

    def test_shieldUniformity(self):
        self.buildTested = 0
        attr = "shieldUniformity"
        iLvl = 1
        iIngame = 0.8
        fLvl = 4
        fIngame = 0.95
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl))
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl))
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
