#Items from group: Rig Energy Weapon (42 of 42)
from customEffects import boostModListByReq
def drawbackPowerNeedLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "power", "drawback",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)