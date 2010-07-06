#Used by: Ship: Huginn
from customEffects import boostModListByReq
def eliteReconBonusHeavyAssaultLauncherROF1(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "speed", "eliteBonusReconShip1",
                      lambda mod: mod.group.name == "Missile Launcher Heavy Assault",
                      self.item, extraMult = level)