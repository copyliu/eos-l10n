#Variations of item: Large Algid Energy Administrations Unit I (2 of 2)
#Variations of item: Medium Algid Energy Administrations Unit I (2 of 2)
#Variations of item: Small Algid Energy Administrations Unit I (2 of 2)
from customEffects import boostModListByReq
def cpuNeedBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)