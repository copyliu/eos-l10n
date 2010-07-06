import unittest
from model import db
from model.types import Drone

class TestDrone(unittest.TestCase):
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