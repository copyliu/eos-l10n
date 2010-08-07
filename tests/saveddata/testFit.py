import unittest
from model.types import Fit, Character, Module, Ship, User, State, Drone, Implant, Booster
from model import db
import model.db.saveddata.queries
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

    def test_setNotAShip(self):
        f = Fit()
        try:
            f.ship = Ship(db.getItem("Gamma L"))
        except ValueError:
            return
        self.fail("Set Gamma L as ship, was expecting ValueError")

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
            oldSession = model.db.saveddata.queries.saveddata_session
            model.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()

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
            model.db.saveddata.queries.saveddata_session = oldSession

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
        self.assertEquals(f.isCapStable(), True)
        self.assertAlmostEquals(f.capState(), 100, 1)

    def test_capacitorUnstable(self):
        f = Fit()
        f.ship = Ship(db.getItem("Rifter"))
        m = Module(db.getItem("100MN Afterburner I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        self.assertEquals(f.isCapStable(), False)
        self.assertTrue(f.capState() < 15)

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
        s = f.calculateSustainableTank()
        self.assertAlmostEquals(s["shieldRepair"], 3.8, 1)

    def test_capCalcs(self):
        f = Fit()
        f.ship = Ship(db.getItem("Reaper"))
        f.ship.itemModifiedAttributes["capacitorCapacity"] = 125.0
        f.ship.itemModifiedAttributes["rechargeRate"] = 93250
        m = Module(db.getItem("Small Shield Booster I"))
        m.state = State.ACTIVE
        f.modules.append(m)
        self.assertAlmostEquals(f.capState(), 16.6, 1)

