from customEffects import boostModListByReq, multiply
def missileLauncherSpeedMultiplierPassive(self, fitting, state):
    boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                      lambda mod: mod.group.name[0:16] == "Missile Launcher",
                      self.item, helper = multiply, useStackingPenalty = True)