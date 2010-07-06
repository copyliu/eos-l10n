#Used by: All carriers
from customEffects import boostModListByReq
def droneControlUnitCpuNeedBonus(self, fitting):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Drone Control Unit", self.item)