import unittest
from model import db
from model.types import Booster, Fit, User, Ship
import sqlalchemy.orm
import model.db.saveddata.queries

class TestBooster(unittest.TestCase):
    def test_SetInvalidBooster(self):
        try:
            b = Booster(db.getItem("Gamma L"))
        except ValueError:
            return
        self.fail("Expected a ValueError when trying to use Gamma L as a booster")
        
    def test_setValidBooster(self):
        b = Booster(db.getItem("Strong Drop Booster"))
        self.assertEquals(2, b.slot)
        i = 0
        for _ in b.iterSideEffects():
            i+= 1
            
        self.assertEquals(4, i)
        
    def test_testEffectList(self):
        b = Booster(db.getItem("Strong Drop Booster"))
        i = 0
        names = ("boosterTurretFalloffPenalty", "boosterArmorRepairAmountPenalty",
                 "boosterMaxVelocityPenalty", "boosterShieldCapacityPenalty")
        for sideEffect in b.iterSideEffects():
            i += 1
            if not sideEffect.effect.name in names:
                self.fail("Invalid effect " + sideEffect.effect.name)
        
        self.assertEquals(4, i)
        
    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.ship = Ship(db.getItem("Rifter"))
            f.owner = User("boostertest", "testy", False)
            b = Booster(db.getItem("Strong Drop Booster"))
            activate = ("boosterTurretFalloffPenalty", "boosterArmorRepairAmountPenalty")
            for sideEffect in b.iterSideEffects():
                if sideEffect.effect.name in activate:
                    sideEffect.active = True
            
            f.boosters.add(b)
            db.saveddata_session.add(f)
            db.saveddata_session.flush()
            fitID = f.ID
            f1id = id(f)
            b1id = id(b)
            
            #Hack our way through changing the session temporarly
            oldSession = model.db.saveddata.queries.saveddata_session
            model.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()
            
            f = db.getFit(fitID)
            self.assertNotEquals(f1id, id(f))
            i = 0
            for b in f.boosters:
                i += 1
                booster = b
            
            self.assertNotEquals(b1id, id(booster))
            self.assertEquals(i, 1)
            for sideEffect in booster.iterSideEffects():
                    self.assertEquals(sideEffect.effect.name in activate, sideEffect.active)
        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            model.db.saveddata.queries.saveddata_session = oldSession