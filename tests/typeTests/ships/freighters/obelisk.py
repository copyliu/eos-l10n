from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Obelisk"

    # Gallente Freighter Skill Bonus:
    # 5% bonus to cargo hold capacity per level

    def test_gallenteFreighter_capacity_ship(self):
        self.buildTested = 0
        attr = "capacity"
        skill = "Gallente Freighter"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Freighter Skill Bonus:
    # 5% bonus to maximum velocity per level

    def test_gallenteFreighter_maxVelocity_ship(self):
        self.buildTested = 0
        attr = "maxVelocity"
        skill = "Gallente Freighter"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
