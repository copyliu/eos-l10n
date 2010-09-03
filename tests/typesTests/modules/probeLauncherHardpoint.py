import unittest
from eos import db
from eos.types import Module, Fit, Hardpoint
from eos.modifiedAttributeDict import ModifiedAttributeDict

class TestHeatSink(unittest.TestCase):
    def setUp(self):
        self.m = Module(db.getItem("Scan Probe Launcher II"))

    def test_hardpoint(self):
        self.assertEquals(self.m.hardpoint, Hardpoint.NONE)
