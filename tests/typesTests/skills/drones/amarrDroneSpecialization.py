from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        self.skill = "Amarr Drone Specialization"

    def test_damageMultiplier_droneWithSkillrq(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Acolyte II"
        iLvl = 1
        iIngame = 1.02
        fLvl = 4
        fIngame = 1.08
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_damageMultiplier_droneCombatNoSkillrq(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Acolyte I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
