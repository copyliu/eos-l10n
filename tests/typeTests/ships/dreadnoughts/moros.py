from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Moros"

    # Gallente Dreadnought Skill Bonus:
    # 5% bonus to Capital Hybrid Turret damage

    def test_gallenteDreadnought_damageMultiplier_moduleHybridWeaponCapital(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Dual 1000mm Railgun I"
        skill = "Gallente Dreadnought"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_damageMultiplier_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Neutron Blaster Cannon I"
        skill = "Gallente Dreadnought"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Dreadnought Skill Bonus:
    # 20% bonus to drone hitpoints per skill level

    def test_gallenteDreadnought_hp_droneCombat(self):
        self.buildTested = 0
        item = "Valkyrie I"
        skill = "Gallente Dreadnought"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_hp_droneLogistic(self):
        self.buildTested = 0
        item = "Heavy Shield Maintenance Bot I"
        skill = "Gallente Dreadnought"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_hp_droneEwar(self):
        self.buildTested = 0
        item = "Ogre SD-900"
        skill = "Gallente Dreadnought"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_hp_droneCapDrain(self):
        self.buildTested = 0
        item = "Acolyte EV-300"
        skill = "Gallente Dreadnought"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_hp_droneWeb(self):
        self.buildTested = 0
        item = "Berserker SW-900"
        skill = "Gallente Dreadnought"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_hp_droneMining(self):
        self.buildTested = 0
        item = "Harvester Mining Drone"
        skill = "Gallente Dreadnought"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Dreadnought Skill Bonus:
    # 20% bonus to drone damage per skill level

    def test_gallenteDreadnought_damageMultiplier_droneCombat(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Curator I"
        skill = "Gallente Dreadnought"
        iLvl = 1
        iIngame = 1.2
        fLvl = 4
        fIngame = 1.8
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteDreadnought_damageMultiplier_other(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Gatling Pulse Laser I"
        skill = "Gallente Dreadnought"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
