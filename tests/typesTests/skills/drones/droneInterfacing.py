from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Drone Interfacing"

    def test_damageMultiplier_droneCombatWithDroneSkillrq(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Hobgoblin II"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_damageMultiplier_droneCombatNoDroneSkillrq(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Einherji"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_miningAmount_droneMining(self):
        self.buildTested = 0
        attr = "miningAmount"
        item = "Harvester Mining Drone"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_miningAmount_other(self):
        self.buildTested = 0
        attr = "miningAmount"
        item = "Miner II"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
