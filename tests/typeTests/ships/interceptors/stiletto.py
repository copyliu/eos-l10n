from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Stiletto"

    def test_minmatarFrigate_damageMultiplier_moduleHybridWeaponSmall(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "200mm AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_damageMultiplier_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "220mm Vulcan AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_trackingSpeed_moduleHybridWeaponSmall(self):
        self.buildTested = 0
        attr = "trackingSpeed"
        item = "125mm Gatling AutoCannon I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.075
        fLvl = 4
        fIngame = 1.3
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_minmatarFrigate_trackingSpeed_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "trackingSpeed"
        item = "720mm Howitzer Artillery I"
        skill = "Minmatar Frigate"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_interceptors_signatureRadiusBonus_moduleAfterburnerSkillrqHighSpeedManeuvering(self):
        self.buildTested = 0
        attr = "signatureRadiusBonus"
        item = "1MN MicroWarpdrive I"
        skill = "Interceptors"
        iLvl = 1
        iIngame = 0.85
        fLvl = 4
        fIngame = 0.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_interceptors_signatureRadiusBonus_moduleOther(self):
        self.buildTested = 0
        attr = "signatureRadiusBonus"
        item = "Target Painter I"
        skill = "Interceptors"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_interceptors_maxRange_moduleWarpScramblerSkillrqPropJamming(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Warp Disruptor I"
        skill = "Interceptors"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_interceptors_maxRange_moduleWarpScramblerNoSkillrqPropJamming(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Civilian Warp Disruptor"
        skill = "Interceptors"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_interceptors_maxRange_moduleOtherSkillrqPropJamming(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Stasis Webifier I"
        skill = "Interceptors"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_role_capacitorNeed_moduleStasisWebSkillrqPropulsionJamming(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Stasis Webifier I"
        ship_other = "Rifter"
        iIngame = 1.0
        fIngame = 0.2
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_role_capacitorNeed_moduleStasisWebNoSkillrqPropulsionJamming(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Civilian Stasis Webifier"
        ship_other = "Rifter"
        iIngame = 1.0
        fIngame = 0.2
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_role_capacitorNeed_moduleWarpScramblerSkillrqPropulsionJamming(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Warp Scrambler I"
        ship_other = "Rifter"
        iIngame = 1.0
        fIngame = 0.2
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_role_capacitorNeed_moduleWarpScramblerNoSkillrqPropulsionJamming(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Civilian Warp Disruptor"
        ship_other = "Rifter"
        iIngame = 1.0
        fIngame = 0.2
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_role_capacitorNeed_moduleOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Ship Scanner I"
        ship_other = "Rifter"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
