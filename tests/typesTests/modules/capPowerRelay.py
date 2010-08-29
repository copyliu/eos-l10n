import unittest
from eos import db
from eos.types import Module, Fit, Ship, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestCapPowerRelay(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.rifter = db.getItem("Rifter")
        self.fit.ship = Ship(self.rifter)
        self.relay = Module(db.getItem("Capacitor Power Relay I"))
        self.fit.modules.append(self.relay)
        self.fit.calculateModifiedAttributes()

    def test_CalcCrash(self):
        # Note, no calculation checking, just testing for a crash here.
        pass
