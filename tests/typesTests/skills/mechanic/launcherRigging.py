from eos.tests import TestBase

class Test(TestBase):
    def setUp(self):
        TestBase.setUp(self)
        self.skill = "Launcher Rigging"

    def test_drawback_moduleRigLauncher(self):
        self.buildTested = 0
        attr = "drawback"
        item = "Small Warhead Rigor Catalyst I"
        iLvl = 1
        iIngame = 0.9
        fLvl = 4
        fIngame = 0.6
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)

    def test_drawback_moduleRigOther(self):
        self.buildTested = 0
        attr = "drawback"
        item = "Medium Drone Speed Augmentor I"
        iLvl = 1
        iIngame = 1.0
        fLvl = 4
        fIngame = 1.0
        iEos = self.skillTestGetItemAttr(self.skill, iLvl, item, attr)
        fEos = self.skillTestGetItemAttr(self.skill, fLvl, item, attr)
        dIngame = fIngame / iIngame
        dEos = fEos / iEos
        self.assertAlmostEquals(dEos, dIngame)
