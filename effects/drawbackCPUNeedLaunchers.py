#Items from group: Rig Launcher (36 of 36)
from customEffects import boostModListByReq
def drawbackCPUNeedLaunchers(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "drawback",
                      lambda mod: mod.group.name[0:16] == "Missile Launcher",
                      self.item)