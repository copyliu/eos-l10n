from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "EM Armor Compensation"

    def test_emDamageResistanceBonus_moduleArmorCoatingSkillrqHullUpgrades(self):
        self.buildTested = 0
        attr = "emDamageResistanceBonus"
        item = "Reflective Plating I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamageResistanceBonus_moduleArmorCoatingSkillrqMechanic(self):
        self.buildTested = 0
        attr = "emDamageResistanceBonus"
        item = "Basic Reflective Plating"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamageResistanceBonus_moduleArmorPlatinEnergized(self):
        self.buildTested = 0
        attr = "emDamageResistanceBonus"
        item = "Energized Reflective Membrane I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_emDamageResistanceBonus_moduleOtherSkillrqHullUpgrades(self):
        self.buildTested = 0
        attr = "emDamageResistanceBonus"
        item = "Armor EM Hardener I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_passiveEmDamageResistanceBonus_moduleArmorHardener(self):
        self.buildTested = 0
        attr = "passiveEmDamageResistanceBonus"
        item = "Armor EM Hardener I"
        iLvl = 1
        iIngame = 3.0
        fLvl = 4
        fIngame = 12.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_passiveEmDamageResistanceBonus_moduleOther(self):
        self.buildTested = 0
        attr = "passiveEmDamageResistanceBonus"
        item = "Photon Scattering Field I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
