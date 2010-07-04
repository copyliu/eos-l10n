#Used by: Item: Hardwiring - 'Prospector' PPZ-X
from customEffects import boostModListByReq
def dataminerModuleDurationReduction(self, fitting):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: mod.group.name == "Data Miners", self.item)