import unittest
from eos.types import Fit, Character, Slot, Module, Ship, User, State, Drone, Implant, Booster, Hardpoint
from eos import db
import eos.db.saveddata.queries
import sqlalchemy.orm
from copy import deepcopy
from itertools import count

class TestFit(unittest.TestCase):
    def setUp(self):
        self.m = Module(db.getItem("Heat Sink I"))

    def test_setCharacter(self):
        f = Fit()
        f.character = Character("Testety")


    def test_addNotAModule(self):
        try:
            self.f.addModule(1302)
        except:
            return
        self.fail("Added an invalid module, was expecting a ValueError")

    def test_addValidModule(self):
        f = Fit()
        f.modules.append(self.m)

    def test_removeModuleNotExists(self):
        f = Fit()
        self.assertRaises(ValueError, f.modules.remove, self.m)

    def test_removeModuleExists(self):
        f = Fit()
        f.modules.append(self.m)
        f.modules.remove(self.m)

    def test_removeInvalidModule(self):
        f = Fit()
        self.assertRaises(ValueError, f.modules.remove, 1302)

    def test_setShip(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))

    def test_extraAttributesClear(self):
        f = Fit()
        f.extraAttributes["cloaked"] = True
        f.clear()
        self.assertEqual(f.extraAttributes["cloaked"], False)

    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.ship = Ship(db.getItem("Rifter"))
            f.name = "test fit 1"
            u = User("fittest", "testy", False)
            f.owner = u

            f2 = Fit()
            f2.ship = Ship(db.getItem("Thrasher"))
            f2.name = "test fit 2"
            f2.owner = u
            db.saveddata_session.add(f)
            db.saveddata_session.add(f2)
            db.saveddata_session.flush()

            f.projectedFits.append(f2)

            #Hack our way through changing the session temporarly
            oldSession = eos.db.saveddata.queries.saveddata_session
            eos.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()

            newf = db.getFit(f.ID)

            self.assertNotEquals(id(newf), id(f))
            self.assertEquals(f.name, newf.name)
            for fit in newf.projectedFits:
                self.assertNotEqual(id(fit), id(f2))
                self.assertEquals(f2.name, fit.name)



        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            eos.db.saveddata.queries.saveddata_session = oldSession

    def test_projectedFit(self):
        f1 = Fit()
        f1.ship = Ship(db.getItem("Rifter"))
        f2 = Fit()
        m1 = Module(db.getItem("Stasis Webifier I"))
        m2 = Module(db.getItem("Stasis Webifier I"))
        m1.state = State.ACTIVE
        m2.state = State.ACTIVE
        f2.modules.append(m1)
        f2.modules.append(m2)
        f1.projectedFits.append(f2)
        f1.calculateModifiedAttributes()
        self.assertAlmostEquals(99.800, f1.ship.getModifiedItemAttr("maxVelocity"), 3)

    def test_projectSelf(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        m1 = Module(db.getItem("Stasis Webifier I"))
        m2 = Module(db.getItem("Stasis Webifier I"))
        m1.state = State.ACTIVE
        m2.state = State.ACTIVE
        f.modules.append(m1)
        f.modules.append(m2)
        f.projectedFits.append(f)
        f.calculateModifiedAttributes()
        self.assertAlmostEquals(99.800, f.ship.getModifiedItemAttr("maxVelocity"), 3)

    def test_capacitorNoMods(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        self.assertEquals(f.capStable, True)
        self.assertAlmostEquals(f.capState, 100, 1)

    def test_capacitorUnstable(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        m = Module(db.getItem("100MN Afterburner I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        self.assertFalse(f.capStable)
        self.assertTrue(f.capState < 15)

    def test_capacitorSingleCycleKill(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        for i in xrange(5):
            m = Module(db.getItem("100MN Afterburner I"))
            m.state = State.ACTIVE
            f.modules.append(m)

        self.assertFalse(f.capStable)
        self.assertEquals(f.capState, 0)

    def test_copy(self):
        f = Fit()
        f.name = "Testety"
        f.character = Character("TEST")
        f.owner = User("moo")
        testm = Module(db.getItem("Heat Sink I"))
        f.modules.append(testm)
        tests = Ship(db.getItem("Rifter"))

        f.ship = tests

        testpm = Module(db.getItem("Stasis Webifier I"))
        f.projectedModules.append(testpm)

        testd = Drone(db.getItem("Hobgoblin I"))
        f.drones.append(testd)

        testi = Implant(db.getItem("Halo Omega"))
        f.implants.append(testi)

        testb = Booster(db.getItem("Strong Drop Booster"))
        f.boosters.append(testb)

        testpd = Drone(db.getItem("Warrior TP-300"))
        f.projectedDrones.append(testpd)

        testpf = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.name = "Projected"
        f.projectedFits.append(testpf)

        newf = deepcopy(f)
        self.assertEquals(newf.name, "%s copy" % f.name)
        self.assertEquals(newf.character, f.character)
        self.assertEquals(newf.owner, f.owner)

        newm = newf.modules[0]
        self.assertNotEquals(id(newm), id(testm))
        self.assertEquals(len(newf.modules), len(f.modules))

        newpm = newf.projectedModules[0]
        self.assertNotEquals(id(newpm), id(testpm))
        self.assertEquals(len(newf.projectedModules), len(f.projectedModules))

        newd = newf.drones[0]
        self.assertNotEquals(id(newd), id(testd))
        self.assertEquals(len(newf.drones), len(f.drones))

        newb = newf.boosters[0]
        self.assertNotEquals(id(newb), id(testb))
        self.assertEquals(len(newf.boosters), len(f.boosters))

        newi = newf.implants[0]
        self.assertNotEquals(id(newi), id(testi))
        self.assertEquals(len(newf.implants), len(f.implants))

        newpd = newf.projectedDrones[0]
        self.assertNotEquals(id(newpd), id(testpd))
        self.assertEquals(len(newf.projectedDrones), len(f.projectedDrones))

        newpm = newf.projectedModules[0]
        self.assertNotEquals(id(newpm), id(testpm))
        self.assertEquals(len(newf.projectedModules), len(f.projectedModules))

        newpf = newf.projectedFits[0]
        self.assertEquals(id(newpf), id(testpf))
        self.assertEquals(len(newf.projectedFits), len(f.projectedFits))

    def test_repperSustainability(self):
        f = Fit()
        f.ship = Ship(db.getItem("Raven"))
        m = Module(db.getItem("Small Shield Booster I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        f.calculateModifiedAttributes()
        s = f.calculateSustainableTank()
        self.assertEquals(s["armorRepair"], f.extraAttributes["armorRepair"])

    def test_ZeroSustainable(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        for i in count(1):
            if i == 5: break
            m = Module(db.getItem("Heavy Energy Neutralizer I"))
            m.state = State.ACTIVE
            f.modules.append(m)

        m = Module(db.getItem("Small Shield Booster I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        f.calculateModifiedAttributes()
        s = f.calculateSustainableTank()
        self.assertEquals(s["armorRepair"], 0)

    def test_sustainabilityConsistency(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        for i in count(1):
            if i == 3: break
            m = Module(db.getItem("Small Shield Booster I"))
            m.state = State.ACTIVE
            f.modules.append(m)

        f.calculateModifiedAttributes()
        s = f.sustainableTank
        self.assertAlmostEquals(s["shieldRepair"], 3.8, 1)

    def test_capCalcs(self):
        f = Fit()
        f.ship = Ship(db.getItem("Reaper"))
        f.ship.itemModifiedAttributes["capacitorCapacity"] = 125.0
        f.ship.itemModifiedAttributes["rechargeRate"] = 93250
        m = Module(db.getItem("Small Shield Booster I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        self.assertAlmostEquals(f.capState, 16.0, 1)

    def test_weaponDPS(self):
        f = Fit()
        m = Module(db.getItem("Heavy Modulated Energy Beam I"))
        m.state = State.ACTIVE
        m.charge = db.getItem("Multifrequency M")
        f.modules.append(m)
        expected = 0
        for type in ("emDamage", "thermalDamage", "kineticDamage", "explosiveDamage"):
            expected += m.getModifiedChargeAttr(type)

        expected *= m.getModifiedItemAttr("damageMultiplier") / (m.getModifiedItemAttr("speed") / 1000.0)
        self.assertAlmostEquals(f.weaponDPS, expected)

    def test_weaponVolley(self):
        f = Fit()
        m = Module(db.getItem("Heavy Modulated Energy Beam I"))
        m.state = State.ACTIVE
        m.charge = db.getItem("Multifrequency M")
        f.modules.append(m)
        expected = 0
        for type in ("emDamage", "thermalDamage", "kineticDamage", "explosiveDamage"):
            expected += m.getModifiedChargeAttr(type)

        expected *= m.getModifiedItemAttr("damageMultiplier")
        self.assertAlmostEquals(f.weaponVolley, expected)

    def test_droneDPS(self):
        f = Fit()
        d = Drone(db.getItem("Hammerhead II"))
        d.active = True
        d.amount = 3
        f.drones.append(d)
        expected = 0
        for type in ("emDamage", "thermalDamage", "kineticDamage", "explosiveDamage"):
            expected += d.getModifiedItemAttr(type)

        expected *= d.getModifiedItemAttr("damageMultiplier") / (d.getModifiedItemAttr("speed") / 1000.0)
        self.assertAlmostEquals(f.droneDPS, expected * 3)

    def test_missileDroneDPS(self):
        f = Fit()
        d = Drone(db.getItem("Cyclops"))
        d.active = True
        d.amount = 2
        f.drones.append(d)
        expected = 0
        for type in ("emDamage", "thermalDamage", "kineticDamage", "explosiveDamage"):
            expected += d.getModifiedChargeAttr(type)

        expected /= d.getModifiedItemAttr("missileLaunchDuration") / 1000.0
        self.assertAlmostEquals(f.droneDPS, expected * 2)

    def test_hardpointCount(self):
        f = Fit()
        f.modules.append(Module(db.getItem("Heavy Modulated Energy Beam I")))
        f.modules.append(Module(db.getItem("Standard Missile Launcher I")))
        f.modules.append(Module(db.getItem("Salvager I")))
        self.assertEquals(f.getHardpointsUsed(Hardpoint.MISSILE), 1)
        self.assertEquals(f.getHardpointsUsed(Hardpoint.TURRET), 1)

    def test_fill(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.fill()
        self.assertEquals(len(f.modules), 13)

    def test_fillT3(self):
        f = Fit()
        f.ship = Ship(db.getItem("Tengu"))
        f.fill()
        self.assertEquals(len(f.modules), 8)

    def test_fillTooMuchDummies(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        for i in xrange(5):
            f.modules.append(Module.buildEmpty(Slot.LOW))

        f.fill()
        self.assertEquals(len(f.modules), 13)

    def test_getSlotsUsed(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.modules.append(Module(db.getItem("Salvager I")))
        f.fill()
        self.assertEquals(f.getSlotsUsed(Slot.HIGH), 1)

    def test_getCalibrationUsed(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.modules.append(Module(db.getItem("Large Trimark Armor Pump I")))
        self.assertEquals(f.calibrationUsed, 50)

    def test_pgUsed(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.modules.append(Module(db.getItem("Salvager I")))
        self.assertEquals(f.pgUsed, 1)

    def test_cpuUsed(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.modules.append(Module(db.getItem("Salvager I")))
        self.assertEquals(f.cpuUsed, 20)

    def test_droneBandwidthUsed(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.drones.append(Drone(db.getItem("Hobgoblin I")))
        self.assertEquals(f.droneBandwidthUsed, 5)

    def test_droneBayUsed(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        f.drones.append(Drone(db.getItem("Hobgoblin I")))
        self.assertEquals(f.droneBayUsed, 5)

    def test_cargoSpace(self):
        f = Fit()
        rifter = db.getItem("Rifter")
        f.ship = Ship(rifter)
        self.assertEquals(f.extraAttributes["capacity"], rifter.capacity)

    def test_addRemoveFit(self):
        f = Fit()
        rifter = db.getItem("Rifter")
        f.ship = Ship(rifter)
        f.fill()
        db.saveddata_session.add(f)
        db.saveddata_session.flush()
        db.saveddata_session.delete(f)
        db.saveddata_session.flush()
