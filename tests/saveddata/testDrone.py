import unittest
from model import db
from model.types import Drone, Fit, User
import model.db.saveddata.queries
import sqlalchemy.orm

class TestDrone(unittest.TestCase):
    def test_DroneNoCharges(self):
        try:
            d = Drone(db.getItem("Hobgoblin I"))
            d.charge = db.getItem("Gamma L")
        except ValueError:
            return
        
        self.fail("Expected a valueError when putting Gamma L in a drone")
    def test_DroneInvalidCharge(self):
        try:
            d = Drone(db.getItem("Cyclops"))
            d.charge = db.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Expected a ValueError when putting Gamma L in a drone")
        
    def test_DroneValidCharge(self):
        d = Drone(db.getItem("Cyclops"))
        d.charge = db.getItem("Compact Purgatory Torpedo I")
        
    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.owner = User("dronetest", "testy", False)
            f.ship = db.getItem("Rifter")
            i = db.getItem("Hobgoblin I")
            d = f.addDroneItemAmount(i, 5)
            
            
            f1id = id(f)
            d1id = id(d)
            
            db.saveddata_session.add(f)
            db.saveddata_session.add(d)
            db.saveddata_session.flush()
            
            fitID = f.ID
            
            #Hack our way through changing the session temporarly
            oldSession = model.db.saveddata.queries.saveddata_session
            model.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()
            
            f = db.getFit(fitID)
            self.assertNotEquals(id(f), f1id)
            
            
            c = 0
            for d in f.iterDrones():
                c += 1
                self.assertNotEquals(id(d), d1id)
            
            self.assertEquals(c, 1)
            self.assertEquals(d.item.ID, i.ID)
            self.assertEquals(d.amount, 5)
            
        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            model.db.saveddata.queries.saveddata_session = oldSession
        