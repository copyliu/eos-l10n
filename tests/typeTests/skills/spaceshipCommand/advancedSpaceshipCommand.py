"""
All bonuses are applied through shipAdvancedSpaceshipCommandAgilityBonus effect,
which is assigned to certain ships, not skill, so skill's effect is actually not used
and range of affected ships broader than just t1 freighters (they're only with direct
skill requirement)
"""

from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Advanced Spaceship Command"

    def test_agility_shipCarrier(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Thanatos"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipDreadnought(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Naglfar"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipFreighter(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Providence"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipJumpFreighter(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Anshar"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipSupercarrier(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Wyvern"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipTitan(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Erebus"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipCapitalIndustrial(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Rorqual"
        iLvl = 1
        iIngame = 0.95
        fLvl = 4
        fIngame = 0.8
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_agility_shipOther(self):
        self.buildTested = 0
        attr = "agility"
        ship = "Apocalypse"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.getShipAttr(attr, skill=(self.skill, iLvl), ship=ship)
        fEos = self.getShipAttr(attr, skill=(self.skill, fLvl), ship=ship)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
