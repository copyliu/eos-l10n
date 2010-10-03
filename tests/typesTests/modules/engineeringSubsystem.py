import unittest
from eos import db
from eos.types import Module, Fit, Ship, State
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestEngineeringSubsystem(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.tengu = db.getItem("Tengu")
        self.fit.ship = Ship(self.tengu)
        self.sub = Module(db.getItem("Tengu Engineering - Augmented Capacitor Reservoir"))
        self.fit.modules.append(self.sub)
        self.fit.calculateModifiedAttributes()

    def test_hardening(self):
        print self.fit.ship.getModifiedItemAttr("powerOutput")
        self.assertGreater(self.fit.ship.getModifiedItemAttr("powerOutput"), 0)
