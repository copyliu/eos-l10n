from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Shield Operation"

    def test_shieldRechargeRate_ship(self):
        self.buildTested = 0
        attr = "shieldRechargeRate"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl))
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl))
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_shieldRechargeRate_subsystem(self):
        self.buildTested = 0
        attr = "shieldRechargeRate"
        item = "Tengu Defensive - Amplification Node"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl))
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl))
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
