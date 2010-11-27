from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.ship = "Guardian"

    def test_amarrCruiser_powerTransferRange_moduleEnergyTransfer(self):
        self.buildTested = 0
        attr = "powerTransferRange"
        item = "Large Energy Transfer Array I"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 2.5
        fLvl = 4
        fIngame = 7.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_powerTransferRange_moduleEnergyTransferCapital(self):
        self.buildTested = 0
        attr = "powerTransferRange"
        item = "Capital Energy Transfer Array I"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 2.5
        fLvl = 4
        fIngame = 7.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_powerTransferRange_moduleOther(self):
        self.buildTested = 0
        attr = "powerTransferRange"
        item = "Medium Nosferatu I"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_maxRange_moduleRemoteArmorRepairer(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Large Remote Armor Repair System I"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 2.5
        fLvl = 4
        fIngame = 7.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_maxRange_moduleRemoteArmorRepairerCapital(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Capital Remote Armor Repair System I"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 2.5
        fLvl = 4
        fIngame = 7.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_maxRange_moduleRemoteArmorRepairerCivilian(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Civilian Remote Armor Repair System"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 2.5
        fLvl = 4
        fIngame = 7.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_maxRange_moduleOther(self):
        self.buildTested = 0
        attr = "maxRange"
        item = "Dual Light Beam Laser I"
        skill = "Amarr Cruiser"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_armorDamageAmount_droneLogistics(self):
        self.buildTested = 0
        attr = "armorDamageAmount"
        item = "Light Armor Maintenance Bot I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 2.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_amarrCruiser_armorDamageAmount_other(self):
        self.buildTested = 0
        attr = "armorDamageAmount"
        item = "Medium Armor Repairer I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_logistics_capacitorNeed_moduleEnergyTransfer(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Small Energy Transfer Array I"
        skill = "Logistics"
        iLvl = 1
        iIngame = 0.85
        fLvl = 4
        fIngame = 0.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_logistics_capacitorNeed_moduleEnergyTransferCapital(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Capital Energy Transfer Array I"
        skill = "Logistics"
        iLvl = 1
        iIngame = 0.85
        fLvl = 4
        fIngame = 0.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_logistics_capacitorNeed_moduleRemoteArmorRepairer(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Medium Remote Armor Repair System I"
        skill = "Logistics"
        iLvl = 1
        iIngame = 0.85
        fLvl = 4
        fIngame = 0.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_logistics_capacitorNeed_moduleRemoteArmorRepairerCapital(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Capital Remote Armor Repair System I"
        skill = "Logistics"
        iLvl = 1
        iIngame = 0.85
        fLvl = 4
        fIngame = 0.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_logistics_capacitorNeed_moduleRemoteArmorRepairerCivilian(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Civilian Remote Armor Repair System"
        skill = "Logistics"
        iLvl = 1
        iIngame = 0.85
        fLvl = 4
        fIngame = 0.4
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_logistics_capacitorNeed_moduleOther(self):
        self.buildTested = 0
        attr = "capacitorNeed"
        item = "Small Energy Neutralizer I"
        skill = "Logistics"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, skill=(skill, iLvl), ship=self.ship)
        fEos = self.getItemAttr(attr, item, skill=(skill, fLvl), ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_special_power_moduleRemoteArmorRepairer(self):
        self.buildTested = 0
        attr = "power"
        item = "Large Remote Armor Repair System I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 0.35
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_special_power_moduleRemoteArmorRepairerCapital(self):
        self.buildTested = 0
        attr = "power"
        item = "Capital Remote Armor Repair System I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 0.35
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_special_power_moduleRemoteArmorRepairerCivilian(self):
        self.buildTested = 0
        attr = "power"
        item = "Civilian Remote Armor Repair System"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 0.35
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_special_power_moduleEnergyTransfer(self):
        self.buildTested = 0
        attr = "power"
        item = "Medium Energy Transfer Array I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 0.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_special_power_moduleEnergyTransferCapital(self):
        self.buildTested = 0
        attr = "power"
        item = "Capital Energy Transfer Array I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 0.5
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_special_power_moduleOther(self):
        self.buildTested = 0
        attr = "power"
        item = "Large Armor Repairer I"
        ship_other = "Omen"
        iIngame = 1.0
        fIngame = 1.0
        iEos = self.getItemAttr(attr, item, ship=ship_other)
        fEos = self.getItemAttr(attr, item, ship=self.ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
