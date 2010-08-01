import unittest
from model import db
from model.types import Module, Fit
from model.modifiedAttributeDict import ModifiedAttributeDict

class TestHeatSink(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.hsi = db.getItem("Heat Sink II")
        self.eti = db.getItem("Heavy Modulated Energy Beam I")
        self.hsm1 = Module(self.hsi)
        self.hsm2 = Module(self.hsi)
        self.etm = Module(self.eti)
        self.fit.modules.append(self.hsm1)
        self.fit.modules.append(self.hsm2)
        self.fit.modules.append(self.etm)
        self.fit.calculateModifiedAttributes()

    def test_damageMultiplier(self):
        original = self.etm.item.getAttribute("damageMultiplier")
        expected = ModifiedAttributeDict()
        expected.original = self.etm.item.attributes
        expected.multiply("damageMultiplier", self.hsi.getAttribute("damageMultiplier"), stackingPenalties = True)
        expected.multiply("damageMultiplier", self.hsi.getAttribute("damageMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["damageMultiplier"], self.etm.getModifiedItemAttr("damageMultiplier"))

    def test_speed(self):
        original = self.etm.item.getAttribute("speed")
        expected = ModifiedAttributeDict()
        expected.original = self.etm.item.attributes
        expected.multiply("speed", self.hsi.getAttribute("speedMultiplier"), stackingPenalties = True)
        expected.multiply("speed", self.hsi.getAttribute("speedMultiplier"), stackingPenalties = True)
        self.assertAlmostEquals(expected["speed"], self.etm.getModifiedItemAttr("speed"))
