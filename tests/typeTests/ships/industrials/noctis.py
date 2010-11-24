from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Noctis"

    def test_oreIndustrial_duration_moduleTractorBeamSkillrqScience(self):
        self.buildTested = 0
        attr = "duration"
        item = "Small Tractor Beam I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_oreIndustrial_duration_moduleOther(self):
        self.buildTested = 0
        attr = "duration"
        item = "Passive Targeter I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_oreIndustrial_duration_moduleDataMinerSkillrqSalvaging(self):
        self.buildTested = 0
        attr = "duration"
        item = "Salvager I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_oreIndustrial_duration_moduleDataMinerSkillrqOther(self):
        self.buildTested = 0
        attr = "duration"
        item = "Analyzer I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_oreIndustrial_maxRange_moduleTractorBeamSkillrqScience(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Small Tractor Beam I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 1.6
        fLvl = 4
        fIngame = 3.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_oreIndustrial_maxRange_moduleOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "200mm Railgun I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_oreIndustrial_maxTractorVelocity_moduleTractorBeamSkillrqScience(self):
        self.buildTested = 0
        attr = "maxTractorVelocity"
        item = "Small Tractor Beam I"
        skill = "ORE Industrial"
        iLvl = 1
        iIngame = 1.6
        fLvl = 4
        fIngame = 3.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
