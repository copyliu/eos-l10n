#Items from group: Rig Hybrid Weapon (42 of 42) [Module]
from customEffects import boostModListByReq
def drawbackPowerNeedHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "power", "drawback",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item)