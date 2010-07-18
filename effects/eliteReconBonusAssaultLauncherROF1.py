#Item: Huginn [Ship]
#Item: Lachesis [Ship]
from customEffects import boostModListByReq
def eliteReconBonusAssaultLauncherROF1(self, fitting):
    skill, level = fitting.getCharSkill("Recon Ships")
    boostModListByReq(fitting.modules, "speed", "eliteBonusReconShip1",
                      lambda mod: mod.group.name == "Missile Launcher Assault",
                      self.item, extraMult = level)