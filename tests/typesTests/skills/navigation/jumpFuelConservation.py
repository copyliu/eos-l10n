from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Jump Fuel Conservation"

    def test_jumpDriveConsumptionAmount_ship(self):
        self.buildTested = 0
        attr = "jumpDriveConsumptionAmount"
        ship = "Thanatos"
        iLvl = 1
        iIngame = 0.9
        fLvl = 4
        fIngame = 0.6
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, ship=ship)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
