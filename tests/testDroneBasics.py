import unittest
from model import db
from model.types import Drone

class TestDroneBasics(unittest.TestCase):
    def test_DroneInvalidCharge(self):
        d = Drone()
        item = db.getItem("Cyclops")
        charge = db.getItem("Gamma L")
        try:
            d.item = item
            d.charge = charge
        except ValueError:
            return
        self.fail("Expected a ValueError when putting Gamma L in a drone")
        
    def test_DroneValidCharge(self):
        d = Drone()
        item = db.getItem("Cyclops")
        charge = db.getItem("Compact Purgatory Torpedo I")
        d.item = item
        d.charge = charge