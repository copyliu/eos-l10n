#Used by: All missile related rigs
from customEffects import boostModListByReq
def drawbackCPUNeedLaunchers(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "drawback",
                      lambda mod: mod.group.name[0:16] == "Missile Launcher",
                      self.item)