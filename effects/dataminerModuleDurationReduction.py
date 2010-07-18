#Item: Hardwiring - Poteque Pharmaceuticals 'Prospector' PPZ-1 [Implant]
from customEffects import boostModListByReq
def dataminerModuleDurationReduction(self, fitting):
    boostModListByReq(fitting.modules, "duration", "durationBonus",
                      lambda mod: mod.group.name == "Data Miners", self.item)