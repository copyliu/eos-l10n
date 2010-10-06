from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Defender Missiles"

    def test_maxVelocity_chargeMissileDefender(self):
        self.buildTested = 0
        attr = "maxVelocity"
        item = "Defender I"
        cont = "Rocket Launcher I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_maxVelocity_chargeOther(self):
        self.buildTested = 0
        attr = "maxVelocity"
        item = "Phalanx Rocket"
        cont = "Rocket Launcher I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr, cont=cont)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr, cont=cont)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
