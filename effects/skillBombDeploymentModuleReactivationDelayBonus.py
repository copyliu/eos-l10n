#Item: Bomb Deployment
from customEffects import boostModListByReq
def skillBombDeploymentModuleReactivationDelayBonus(self, fitting, level):
    boostModListByReq(fitting.modules, "moduleReactivationDelay", "rofBonus",
                      lambda mod: mod.group.name == "Missile Launcher Bomb",
                      self.item, extraMult = level)