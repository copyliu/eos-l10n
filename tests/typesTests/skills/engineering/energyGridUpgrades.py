import unittest
from eos import db
from eos.types import Fit, Character, Skill, Ship, Module
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestEnergyGridUpgrades(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.char = Character("testSkill")
        self.skill = db.getItem("Energy Grid Upgrades")
        self.skillLevel = 5
        self.char.addSkill(Skill(self.skill, self.skillLevel))
        self.fit.character = self.char

    def test_cpu_capacitorBattery(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Guardian"))
        self.testItem = db.getItem("Large Capacitor Battery II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorBatteryMicroT1(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Retribution"))
        self.testItem = db.getItem("Micro Ohm Capacitor Reserve I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorFluxCoil(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Paladin"))
        self.testItem = db.getItem("Beta Reactor Control: Capacitor Flux I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorFluxCoilBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Thorax"))
        self.testItem = db.getItem("Type-E Power Core Modification: Capacitor Flux")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorPowerRelay(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Onyx"))
        self.testItem = db.getItem("True Sansha Capacitor Power Relay")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorPowerRelayBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Drake"))
        self.testItem = db.getItem("Marked Generator Refitting: Capacitor Power Relay")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorRecharger(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Onyx"))
        self.testItem = db.getItem("Eutectic I Capacitor Charge Array")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_capacitorRechargerBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Drake"))
        self.testItem = db.getItem("Industrial Capacitor Recharger")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_powerDiagnosticSystem(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Brutix"))
        self.testItem = db.getItem("Power Diagnostic System II")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_powerDiagnosticSystemBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Phoenix"))
        self.testItem = db.getItem("Alpha Reactor Control: Diagnostic System")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_reactorControlUnit(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Imicus"))
        self.testItem = db.getItem("Shadow Serpentis Reactor Control Unit")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_reactorControlUnitBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Purifier"))
        self.testItem = db.getItem("Type-E Power Core Modification: Reaction Control")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_shieldFluxCoil(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Raven"))
        self.testItem = db.getItem("Local Power Plant Manager: Reaction Shield Flux I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_shieldFluxCoilBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Punisher"))
        self.testItem = db.getItem("Alpha Reactor Shield Flux")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_shieldPowerRelay(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Megathron"))
        self.testItem = db.getItem("Shield Power Relay I")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)

    def test_cpu_shieldPowerRelayBasic(self):
        self.buildTested = 0
        self.fit.ship = Ship(db.getItem("Rapier"))
        self.testItem = db.getItem("Basic Shield Power Relay")
        self.testMod = Module(self.testItem)
        self.fit.modules.append(self.testMod)
        self.fit.calculateModifiedAttributes()
        targetAttrName = "cpu"
        skillBonus = self.skill.getAttribute("cpuNeedBonus")
        expected = ModifiedAttributeDict()
        expected.original = self.testItem.attributes
        expected.boost(targetAttrName, skillBonus * self.skillLevel)
        actual = self.testMod.getModifiedItemAttr(targetAttrName)
        self.assertAlmostEquals(expected[targetAttrName], actual)
