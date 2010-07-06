#Used by: Item: Algid Hybrid Administrations Unit
from customEffects import boostModListByReq
def cpuNeedBonusEffectHybrid(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item)