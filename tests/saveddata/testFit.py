import unittest
from model.types import Fit, Character, Module, Ship, User
from model import db
import model.db.saveddata.queries
import sqlalchemy.orm

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
