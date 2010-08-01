import unittest
from model import db
from model.types import Module, Fit, Ship, State
from model.tests.typesTests import calculateBoostMultiplier, calculateMultiplierMultiplier

class TestSignalAmplifier(unittest.TestCase):
    def setUp(self):
        self.fit = Fit()
        self.fit.ship = Ship(db.getItem("Rifter"))
        self.t1tss1m = Module(db.getItem("Small Targeting System Subcontroller I"))
        self.t1tss2m = Module(db.getItem("Small Targeting System Subcontroller I"))
        self.t2tss1m = Module(db.getItem("Small Targeting System Subcontroller II"))
        self.t2tss2m = Module(db.getItem("Small Targeting System Subcontroller II"))

    #T1 and T2 rigs have different effects for scanning resolution boost,
    #so we have to test them separately
    def test_scanResolutionT1(self):
        self.fit.modules.append(self.t1tss1m)
        self.fit.modules.append(self.t1tss2m)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.attributes["scanResolution"].value
        boostList = []
        boostList.append(self.t1tss1m.item.attributes["scanResolutionMultiplier"].value)
        boostList.append(self.t1tss2m.item.attributes["scanResolutionMultiplier"].value)
        expected = original * calculateMultiplierMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("scanResolution"), 3)

    def test_scanResolutionT2(self):
        self.fit.modules.append(self.t2tss1m)
        self.fit.modules.append(self.t2tss2m)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.attributes["scanResolution"].value
        boostList = []
        boostList.append(self.t2tss1m.item.attributes["scanResolutionMultiplier"].value)
        boostList.append(self.t2tss2m.item.attributes["scanResolutionMultiplier"].value)
        expected = original * calculateMultiplierMultiplier(boostList, stackingPenalized = True)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("scanResolution"), 3)

    def test_shieldCapacity(self):
        self.fit.modules.append(self.t1tss1m)
        self.fit.modules.append(self.t2tss2m)
        self.fit.calculateModifiedAttributes()
        original = self.fit.ship.item.attributes["shieldCapacity"].value
        boostList = []
        boostList.append(self.t1tss1m.item.attributes["drawback"].value)
        boostList.append(self.t2tss2m.item.attributes["drawback"].value)
        expected = original * calculateBoostMultiplier(boostList, stackingPenalized = False)
        self.assertAlmostEquals(expected, self.fit.ship.getModifiedItemAttr("shieldCapacity"), 3)


