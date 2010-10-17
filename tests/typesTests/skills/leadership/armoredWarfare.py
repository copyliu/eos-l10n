from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Armored Warfare"

    def test_armorHP_fleetShip(self):
        self.buildTested = 0
        attr = "armorHP"
        iLvl = 1
        iIngame = 1.02
        fLvl = 4
        fIngame = 1.08
        iEos = self.skillTestGetShipAttr(self.skill, iLvl, attr, gang=True)
        fEos = self.skillTestGetShipAttr(self.skill, fLvl, attr, gang=True)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
