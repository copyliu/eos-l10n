from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Ishtar"

    # Gallente Cruiser Skill Bonus:
    # 5% bonus to Medium Hybrid Turret damage per skill level

    def test_gallenteCruiser_damageMultiplier_moduleHybridWeaponMedium(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Heavy Ion Blaster I"
        skill = "Gallente Cruiser"
        iLvl = 1
        iIngame = 1.05
        fLvl = 4
        fIngame = 1.2
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_damageMultiplier_moduleHybridWeaponOther(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Light Neutron Blaster I"
        skill = "Gallente Cruiser"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Gallente Cruiser Skill Bonus:
    # 10% bonus to drone hitpoints per skill level

    def test_gallenteCruiser_hp_droneCombat(self):
        self.buildTested = 0
        item = "Curator I"
        skill = "Gallente Cruiser"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_hp_droneLogistic(self):
        self.buildTested = 0
        item = "Heavy Armor Maintenance Bot I"
        skill = "Gallente Cruiser"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_hp_droneEwar(self):
        self.buildTested = 0
        item = "Vespa EC-600"
        skill = "Gallente Cruiser"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_hp_droneCapDrain(self):
        self.buildTested = 0
        item = "Praetor EV-900"
        skill = "Gallente Cruiser"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_hp_droneWeb(self):
        self.buildTested = 0
        item = "Berserker SW-900"
        skill = "Gallente Cruiser"
        layers = ("shieldCapacity", "armorHP", "hp")
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = 0
        fEos = 0
        for layer in layers:
            iEos += self.getItemAttr(layer, item, skill=(skill, iLvl), ship=self.ship)
            fEos += self.getItemAttr(layer, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_hp_droneMining(self):
        self.buildTested = 0
        item = "Mining Drone I"
        skill = "Gallente Cruiser"
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

    # Gallente Cruiser Skill Bonus:
    # 10% bonus to drone damage per skill level

    def test_gallenteCruiser_damageMultiplier_droneCombat(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Valkyrie I"
        skill = "Gallente Cruiser"
        iLvl = 1
        iIngame = 1.1
        fLvl = 4
        fIngame = 1.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_gallenteCruiser_damageMultiplier_other(self):
        self.buildTested = 0
        attr = "damageMultiplier"
        item = "Dual Light Pulse Laser I"
        skill = "Gallente Cruiser"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Heavy Assault Ship Skill Bonus:
    # +5 km bonus to Scout and Heavy Drone operation range per level

    def test_heavyAssaultShips_droneControlRange_ship(self):
        self.buildTested = 0
        attr = "droneControlRange"
        skill = "Heavy Assault Ships"
        iLvl = 1
        iIngame = 25000.0
        fLvl = 4
        fIngame = 40000.0
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Heavy Assault Ship Skill Bonus:
    # +50 m3 extra Drone Bay space per level

    def test_heavyAssaultShips_droneCapacity_ship(self):
        self.buildTested = 0
        attr = "droneCapacity"
        skill = "Heavy Assault Ships"
        iLvl = 1
        iIngame = 250.0
        fLvl = 4
        fIngame = 400.0
        iEos = self.getShipAttr(attr, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getShipAttr(attr, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
