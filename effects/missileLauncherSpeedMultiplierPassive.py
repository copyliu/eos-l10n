#Variations of item: Large Bay Loading Accelerator I (2 of 2)
#Variations of item: Medium Bay Loading Accelerator I (2 of 2)
#Variations of item: Small Bay Loading Accelerator I (2 of 2)
from customEffects import boostModListByReq, multiply
def missileLauncherSpeedMultiplierPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name[0:16] == "Missile Launcher",
                      self.item, helper = multiply, useStackingPenalty = True)