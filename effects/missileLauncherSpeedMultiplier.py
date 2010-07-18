#Items from group: Ballistic Control system (21 of 21) [Module]
from customEffects import boostModListByReq, multiply
import model.fitting
def missileLauncherSpeedMultiplier(self, fitting, state):
    if state >= model.fitting.STATE_INACTIVE:
        boostModListByReq(fitting.modules, "speed", "speedMultiplier",
                          lambda mod: mod.group.name[0:16] == "Missile Launcher",
                          self.item, helper = multiply, useStackingPenalty = True)