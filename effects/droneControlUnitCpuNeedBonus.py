#Items from group: Carrier (4 of 4) [Ship]
#Items from group: Supercarrier (4 of 4) [Ship]
from customEffects import boostModListByReq
def droneControlUnitCpuNeedBonus(self, fitting):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Drone Control Unit", self.item)