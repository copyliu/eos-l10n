import unittest
from model.types import Character, User, Fit, Skill, Ship
from model import db
import model.db.saveddata.queries
import sqlalchemy.orm

class TestCharacter(unittest.TestCase):
    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.ship = Ship(db.getItem("Rifter"))
            c = Character("testChar")
            f.character = c
            u = User("testChar", "moo", False)
            f.owner = u
            c.owner = u
            c.addSkill(Skill(db.getItem("Caldari Frigate"), 3))
            c.addSkill(Skill(db.getItem("Gallente Frigate"), 1))
            c.addSkill(Skill(db.getItem("Gallente Industrial"), 5))
            db.saveddata_session.add(u)
            db.saveddata_session.add(c)
            db.saveddata_session.add(f)
            db.saveddata_session.flush()
            
            #Hack our way through changing the session temporarly
            oldSession = model.db.saveddata.queries.saveddata_session
            model.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()
            
            newf = db.getFit(f.ID)
            newu = db.getUser(u.ID)
            newc = newu.characters[0]
            self.assertNotEquals(id(newf), id(f))
            self.assertNotEquals(id(newu), id(u))
            self.assertNotEquals(id(newc), id(c))
            self.assertEquals(len(newu.characters), 1)
            self.assertEquals(f.character.ID, newf.character.ID)
            skillDict= {"Caldari Frigate" : 3,
                        "Gallente Frigate" : 1,
                        "Gallente Industrial" : 5}
            for skill in newc.iterSkills():
                self.assertTrue(skillDict.has_key(skill.item.name))
                self.assertEquals(skillDict[skill.item.name], skill.level)
            
            
        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            model.db.saveddata.queries.saveddata_session = oldSession
            
    def test_suppress(self):
        s = Skill(db.getItem("Caldari Frigate"))
        s.suppress()
        self.assertTrue(s.isSuppressed())
        s.clear()
        self.assertFalse(s.isSuppressed())
        
    def test_getSkill(self):
        c = Character("testetyChar")
        s1 = Skill(db.getItem("Caldari Frigate"), 3)
        c.addSkill(s1)
        c.addSkill(Skill(db.getItem("Gallente Frigate"), 1))
        c.addSkill(Skill(db.getItem("Gallente Industrial"), 5))
        self.assertEquals(c.getSkill(s1.item.name), s1)
        self.assertEquals(c.getSkill(s1.item.ID), s1)
        self.assertEquals(c.getSkill(s1.item), s1)