#Items from group: Combat Recon Ship (2 of 4)
from customEffects import boostModListByReq
def eliteReconBonusHeavyLauncherROF1(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "speed", "eliteBonusReconShip1",
                      lambda mod: mod.group.name == "Missile Launcher Heavy",
                      self.item, extraMult = level)