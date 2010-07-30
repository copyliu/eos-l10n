import unittest
from model.types import Module, Fit, User, State, Ship, Slot
from model import db
import model.db.saveddata.queries
import sqlalchemy.orm

class TestModule(unittest.TestCase):
    def setUp(self):
        self.i = db.getItem("Heat Sink I")
        self.m = Module(self.i)

    def test_clear(self):
        m = Module(db.getItem("125mm Gatling AutoCannon I"))
        m.charge = db.getItem("Phased Plasma S")
        orig = m.getModifiedItemAttr("trackingSpeed")
        chargeOrig = m.getModifiedChargeAttr("explosiveDamage")
        m.itemModifiedAttributes["trackingSpeed"] = 5
        m.chargeModifiedAttributes["explosiveDamage"] = 10
        m.clear()
        self.assertEquals(m.getModifiedItemAttr("trackingSpeed"), orig)
        self.assertEquals(m.getModifiedChargeAttr("explosiveDamage"), chargeOrig)

    def test_setItem(self):
        self.assertEquals(self.m.itemID, self.i.ID)

    def test_setPassiveActive(self):
        try:
            self.m.state = State.ACTIVE
        except ValueError:
            return

        self.fail("Expected a ValueError, didn't get it.")

    def test_setPassiveOverload(self):
        try:
            self.m.state = State.OVERHEATED
        except ValueError:
            return

        self.fail("Expected a ValueError, didn't get it.")

    def test_setActiveOverloadWhenGood(self):
        m = Module(db.getItem("Heavy Modulated Energy Beam I"))
        m.state = State.ACTIVE
        m.state = State.OVERHEATED

    def test_setWrongAmmoType(self):
        try:
            m = Module(db.getItem("125mm Gatling AutoCannon I"))
            m.charge = db.getItem("Gamma L")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")

    def test_setWrongAmmoSize(self):
        try:
            m = Module(db.getItem("Dual Light Pulse Laser I"))
            m.charge = db.getItem("Gamma M")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")

    def test_setWrongAmmoSubGroup(self):
        try:
            m = Module(db.getItem("Dual Light Pulse Laser I"))
            m.charge = db.getItem("Scorch S")
        except ValueError:
            return
        self.fail("Expected a ValueError, didn't get it.")

    def test_setCorrectAmmo(self):
        i = db.getItem("Dual Light Pulse Laser I")
        m = Module(i)
        a = db.getItem("Gamma S")
        m.charge = a
        self.assertEquals(m.itemID, i.ID)
        self.assertEquals(m.chargeID, a.ID)

    def test_slotRig(self):
        m = Module(db.getItem("Large Capacitor Control Circuit I"))
        self.assertEquals(Slot.RIG, m.slot)

    def test_slotSubsystem(self):
        m = Module(db.getItem("Tengu Offensive - Magnetic Infusion Basin"))
        self.assertEquals(Slot.SUBSYSTEM, m.slot)

    def test_slotHigh(self):
        m = Module(db.getItem("Salvager I"))
        self.assertEquals(Slot.HIGH, m.slot)

    def test_slotMed(self):
        m = Module(db.getItem("Cap Recharger I"))
        self.assertEquals(Slot.MED, m.slot)

    def test_slotLow(self):
        m = Module(db.getItem("Heat Sink I"))
        self.assertEquals(Slot.LOW, m.slot)

    def test_DatabaseConsistency(self):
        oldSession = db.saveddata_session
        oldSession.commit()
        try:
            f = Fit()
            f.ship = Ship(db.getItem("Rifter"))
            f.owner = User("moduletest", "testy", False)

            item = db.getItem("Dual Light Pulse Laser I")
            item2 = db.getItem("Stasis Webifier I")
            projMod = Module(item2)
            charge = db.getItem("Gamma S")
            mod = Module(item)
            mod.charge = charge
            f.modules.append(mod)
            f.projectedModules.append(projMod)
            db.saveddata_session.add(f)
            db.saveddata_session.flush()

            #Hack our way through changing the session temporarly
            oldSession = model.db.saveddata.queries.saveddata_session
            model.db.saveddata.queries.saveddata_session = sqlalchemy.orm.sessionmaker(bind=db.saveddata_engine)()

            newf = db.getFit(f.ID)
            self.assertNotEquals(id(newf), id(f))

            i = 0
            for m in newf.modules:
                i+= 1
                newmod = m
            
            self.assertEquals(i, 1)
            
            i = 0
            for m in newf.projectedModules:
                i += 1
                newprojMod = m
            
            self.assertEquals(newprojMod.item.name, "Stasis Webifier I")
            self.assertEqual(i, 1)
            self.assertNotEquals(id(newprojMod), id(projMod))
            self.assertNotEquals(id(newmod), id(mod))
            self.assertEquals(mod.state, newmod.state)
            self.assertEquals(mod.charge.ID, newmod.charge.ID)
            self.assertEquals(mod.item.ID, newmod.item.ID)
        except:
            db.saveddata_session.rollback()
            raise
        finally:
            #Undo our hack as to not fuck up anything
            model.db.saveddata.queries.saveddata_session = oldSession
