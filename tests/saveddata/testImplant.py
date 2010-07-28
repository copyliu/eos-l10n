import unittest
from model.types import Implant, Fit, User, Ship
from model import db
import model.db.saveddata.queries
import sqlalchemy.orm

class TestImplant(unittest.TestCase):
    def test_InvalidImplant(self):
        try:
            i = Implant(db.getItem("Gamma L"))
        except ValueError:
            return
        self.fail("Was expected a ValueError when setting Gamma L as implant, didn't get it")

    def test_clear(self):
        i = Implant(db.getItem("Halo Omega"))
        orig = i.getModifiedItemAttr("memoryBonus")

        i.itemModifiedAttributes["memoryBonus"] = 5
        i.clear()
        self.assertEquals(i.getModifiedItemAttr("memoryBonus"), orig)

    def test_validImplant(self):
        i = Implant(db.getItem("Halo Omega"))
        self.assertEquals(i.slot, 6)

    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.owner = User("implanttest", "testy", False)
            f.ship = Ship(db.getItem("Rifter"))
            implant = Implant(db.getItem("Halo Omega"))
            f.implants.append(implant)
            implant.active = False
            db.saveddata_session.add(f)
            db.saveddata_session.add(implant)
            db.saveddata_session.flush()

            #Hack our way through changing the session temporarly
            oldSession = model.db.saveddata.queries.saveddata_session
            model.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()

            newfit = db.getFit(f.ID)
            i = 0
            for imp in newfit.implants:
                newimplant = imp
                i += 1

            self.assertFalse(implant.active)
            self.assertEquals(i, 1)
            self.assertNotEquals(id(f), id(newfit))
            self.assertNotEquals(id(implant), id(newimplant))
            self.assertEquals(implant.fit.ID, newimplant.fit.ID)
            self.assertEquals(implant.item.ID, newimplant.item.ID)

        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            model.db.saveddata.queries.saveddata_session = oldSession
