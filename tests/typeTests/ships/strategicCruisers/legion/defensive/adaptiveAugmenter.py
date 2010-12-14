from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.hull = "Legion"
        self.subsystem = "Legion Defensive - Adaptive Augmenter"

    def test_amarrDefensiveSystems_armorEmDamageResonance_ship(self):
        self.buildTested = 0
        attr = "armorEmDamageResonance"
        skill = "Amarr Defensive Systems"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.hull, miscitms=self.subsystem)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.hull, miscitms=self.subsystem)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
