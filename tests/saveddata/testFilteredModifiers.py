import unittest
from eos import db
from eos.types import Fit, Drone

class TestFilteredModifiers(unittest.TestCase):
    def setUp(self):
        self.f = Fit()
        self.i1 = db.getItem("Cyclops")
        self.i2 = db.getItem("Cyclops")
        self.charge = db.getItem("Compact Purgatory Torpedo I")
        self.f.drones.appendItem(self.i1, 1)
        self.f.drones.appendItem(self.i2, 1)

    def test_FilteredItemIncrease(self):
        self.f.drones.filteredItemIncrease(lambda d: d.item.ID == self.i1.ID, "hp", 5)
        for d in self.f.drones:
            if d.item.ID == self.i1.ID:
                self.assertEquals(d.itemModifiedAttributes["hp"], self.i1.getAttribute("hp") + 5)
            else:
                self.assertEquals(d.itemModifiedAttributes["hp"], self.i2.getAttribute("hp"))


    def test_FilteredItemMultiply(self):
        self.f.drones.filteredItemMultiply(lambda d: d.item.ID == self.i1.ID, "hp", 5)
        for d in self.f.drones:
            if d.item.ID == self.i1.ID:
                self.assertEquals(d.itemModifiedAttributes["hp"], self.i1.getAttribute("hp") * 5)
            else:
                self.assertEquals(d.itemModifiedAttributes["hp"], self.i2.getAttribute("hp"))


    def test_FilteredItemBoost(self):
        self.f.drones.filteredItemBoost(lambda d: d.item.ID == self.i1.ID, "hp", 5)
        for d in self.f.drones:
            if d.item.ID == self.i1.ID:
                self.assertEquals(d.itemModifiedAttributes["hp"], self.i1.getAttribute("hp") * 1.05)
            else:
                self.assertEquals(d.itemModifiedAttributes["hp"], self.i2.getAttribute("hp"))

    def test_FilteredChargeIncrease(self):
        self.f.drones.filteredChargeIncrease(lambda d: d.item.ID == self.i1.ID, "hp", 5)
        for d in self.f.drones:
            if d.item.ID == self.i1.ID:
                self.assertEquals(d.chargeModifiedAttributes["hp"], self.charge.getAttribute("hp") + 5)
            else:
                self.assertEquals(d.chargeModifiedAttributes["hp"], self.charge.getAttribute("hp"))


    def test_FilteredChargeMultiply(self):
        self.f.drones.filteredChargeMultiply(lambda d: d.item.ID == self.i1.ID, "hp", 5)
        for d in self.f.drones:
            if d.item.ID == self.i1.ID:
                self.assertEquals(d.chargeModifiedAttributes["hp"], self.charge.getAttribute("hp") * 5)
            else:
                self.assertEquals(d.chargeModifiedAttributes["hp"], self.charge.getAttribute("hp"))


    def test_FilteredChargeBoost(self):
        self.f.drones.filteredChargeBoost(lambda d: d.item.ID == self.i1.ID, "hp", 5)
        for d in self.f.drones:
            if d.item.ID == self.i1.ID:
                self.assertEquals(d.chargeModifiedAttributes["hp"], self.charge.getAttribute("hp") * 1.05)
            else:
                self.assertEquals(d.chargeModifiedAttributes["hp"], self.charge.getAttribute("hp"))

