import unittest
from model import db
from model.types import Drone, Fit, User, Ship
import model.db.saveddata.queries
import sqlalchemy.orm

class TestDrone(unittest.TestCase):
    def test_clear(self):
        d = Drone(db.getItem("Hobgoblin I"))
        orig = d.getModifiedItemAttr("hp")

        d.itemModifiedAttributes["hp"] = 5
        d.clear()
        self.assertEquals(d.getModifiedItemAttr("hp"), orig)

    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.owner = User("dronetest", "testy", False)
            f.ship = Ship(db.getItem("Rifter"))
            i = db.getItem("Hobgoblin I")
            
            d = f.drones.appendItem(i, 5)
            d.amountActive = 3
            d2 = f.projectedDrones.appendItem(i, 3)
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
            for d in f.drones:
                c += 1
                self.assertNotEquals(id(d), d1id)
            
            self.assertEquals(c, 1)
            self.assertEquals(d.item.ID, i.ID)
            self.assertEquals(d.amount, 5)
            self.assertEquals(d.amountActive, 3)
            
            c = 0
            for d in f.projectedDrones:
                c += 1
                self.assertNotEquals(id(d2), id(d))
                
            self.assertEquals(c, 1)
            self.assertEquals(d.item.ID, i.ID)
            self.assertEquals(d.amount, 3)
        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            model.db.saveddata.queries.saveddata_session = oldSession
