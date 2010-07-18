#Variations of item: Large Algid Hybrid Administrations Unit I (2 of 2) [Module]
#Variations of item: Medium Algid Hybrid Administrations Unit I (2 of 2) [Module]
#Variations of item: Small Algid Hybrid Administrations Unit I (2 of 2) [Module]
from customEffects import boostModListByReq
def cpuNeedBonusEffectHybrid(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item)