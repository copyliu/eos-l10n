#Used by: Legion Electronics - Emergent Locus Analyzer
from customEffects import boostModListByReq
def subsystemBonusScanProbeLauncherCPU(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Scan Probe Launcher",
                      self.item)