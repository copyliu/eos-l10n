from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.hull = "Tengu"
        self.sub = "Tengu Engineering - Supplemental Coolant Injector"
        self.skill = "Caldari Engineering Systems"

    # Subsystem Skill Bonus:
    # 5% Reduction in the amount of heat damage absorbed by modules per level

    def test_caldariEngineeringSystems_heatDamage_moduleAfterburner(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "1MN MicroWarpdrive I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleArmorHardener(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Armor Explosive Hardener I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleRemoteArmorRepairer(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Large Remote Armor Repair System I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleArmorRepairer(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Large Armor Repairer I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleCapacitorBooster(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Medium Capacitor Booster I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleECCM(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "ECCM - Ladar I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleECM(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "ECM - White Noise Generator I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleEnergyDestabilizer(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Heavy Energy Neutralizer I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleEnergyTransferArray(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Large Energy Transfer Array I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleEnergyVampire(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Small Nosferatu I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleEnergyWeapon(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Gatling Pulse Laser I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleHullRepairUnit(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Small Hull Repairer I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleHybridWeapon(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "75mm Gatling Rail I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherAssault(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Assault Missile Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherCitadel(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Citadel Torpedo Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherCruise(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Cruise Missile Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherHeavy(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Heavy Missile Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherHeavyAssault(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Heavy Assault Missile Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherRocket(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Rocket Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherSiege(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Siege Missile Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleMissileLauncherStandard(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Standard Missile Launcher I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleProjectileWeapon(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "800mm Repeating Artillery I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleShieldBooster(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Medium Shield Booster I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleShieldHardener(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Explosion Dampening Field I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleShieldTransporter(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Medium Shield Transporter I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleStasisWeb(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Stasis Webifier I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_caldariEngineeringSystems_heatDamage_moduleWarpScrambler(self):
        self.buildTested = 0
        attr = "heatDamage"
        item = "Warp Disruptor I"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getItemAttr(attr, item, skill=(self.skill, iLvl), ship=self.hull, miscitms=self.sub)
        fEos = self.getItemAttr(attr, item, skill=(self.skill, fLvl), ship=self.hull, miscitms=self.sub)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # Add slots to ship

    def test_static_hiSlots_ship(self):
        self.buildTested = 0
        attr = "hiSlots"
        iIngame = 0.0
        fIngame = 0.0
        iEos = self.getShipAttr(attr, ship=self.hull) or 0.0
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub) or 0.0
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_medSlots_ship(self):
        self.buildTested = 0
        attr = "medSlots"
        iIngame = 0.0
        fIngame = 0.0
        iEos = self.getShipAttr(attr, ship=self.hull) or 0.0
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub) or 0.0
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_lowSlots_ship(self):
        self.buildTested = 0
        attr = "lowSlots"
        iIngame = 0.0
        fIngame = 3.0
        iEos = self.getShipAttr(attr, ship=self.hull) or 0.0
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub) or 0.0
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # Add weapon hardpoints

    def test_static_turretSlotsLeft_ship(self):
        self.buildTested = 0
        attr = "turretSlotsLeft"
        iIngame = 0.0
        fIngame = 0.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_static_launcherSlotsLeft_ship(self):
        self.buildTested = 0
        attr = "launcherSlotsLeft"
        iIngame = 0.0
        fIngame = 0.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +1200000 kg mass

    def test_static_mass_ship(self):
        self.buildTested = 0
        attr = "mass"
        iIngame = 8201000.0
        fIngame = 9401000.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +825 MW powergrid

    def test_static_powerOutput_ship(self):
        self.buildTested = 0
        attr = "powerOutput"
        iIngame = 0.0
        fIngame = 825.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +1225 GJ capacitor capacity

    def test_static_capacitorCapacity_ship(self):
        self.buildTested = 0
        attr = "capacitorCapacity"
        iIngame = 100.0
        fIngame = 1325.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)

    # Hidden bonus:
    # +415 seconds capacitor recharge time

    def test_static_rechargeRate_ship(self):
        self.buildTested = 0
        attr = "rechargeRate"
        iIngame = 10000.0
        fIngame = 425000.0
        iEos = self.getShipAttr(attr, ship=self.hull)
        fEos = self.getShipAttr(attr, ship=self.hull, miscitms=self.sub)
        dIngame = fIngame - iIngame
        dEos = fEos - iEos
        self.assertAlmostEquals(dEos, dIngame)
