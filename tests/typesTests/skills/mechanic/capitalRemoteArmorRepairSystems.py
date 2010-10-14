from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Capital Remote Armor Repair Systems"

    def test_capacitorNeed_moduleArmorRepairProjectorSkillrq(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Capital Remote Armor Repair System I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_capacitorNeed_moduleArmorRepairProjectorNoSkillrq(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Medium Remote Armor Repair System I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
