from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Drone Durability"
        self.layers = ("shieldCapacity", "armorHP", "hp")

    def tearDown(self):
        TestBase.tearDown(self)

    def test_hp_droneCombat(self):
        self.buildTested = 0
        item = "Berserker I"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = 0
        fEos = 0
        for layer in self.layers:
            iEos += self.skillTestGetItemAttr(self.skill, iLvl, item, layer)
            fEos += self.skillTestGetItemAttr(self.skill, fLvl, item, layer)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_hp_droneLogistic(self):
        self.buildTested = 0
        item = "Heavy Shield Maintenance Bot II"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = 0
        fEos = 0
        for layer in self.layers:
            iEos += self.skillTestGetItemAttr(self.skill, iLvl, item, layer)
            fEos += self.skillTestGetItemAttr(self.skill, fLvl, item, layer)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_hp_droneEwar(self):
        self.buildTested = 0
        item = "Wasp EC-900"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = 0
        fEos = 0
        for layer in self.layers:
            iEos += self.skillTestGetItemAttr(self.skill, iLvl, item, layer)
            fEos += self.skillTestGetItemAttr(self.skill, fLvl, item, layer)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_hp_droneCapDrain(self):
        self.buildTested = 0
        item = "Praetor EV-900"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = 0
        fEos = 0
        for layer in self.layers:
            iEos += self.skillTestGetItemAttr(self.skill, iLvl, item, layer)
            fEos += self.skillTestGetItemAttr(self.skill, fLvl, item, layer)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_hp_droneWeb(self):
        self.buildTested = 0
        item = "Berserker SW-900"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = 0
        fEos = 0
        for layer in self.layers:
            iEos += self.skillTestGetItemAttr(self.skill, iLvl, item, layer)
            fEos += self.skillTestGetItemAttr(self.skill, fLvl, item, layer)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_hp_droneOther(self):
        self.buildTested = 0
        item = "Einherji"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = 0
        fEos = 0
        for layer in self.layers:
            iEos += self.skillTestGetItemAttr(self.skill, iLvl, item, layer)
            fEos += self.skillTestGetItemAttr(self.skill, fLvl, item, layer)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
