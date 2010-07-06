#Used by: Item: Algid Energy Administrations Unit
from customEffects import boostModListByReq
def cpuNeedBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "cpu", "cpuNeedBonus",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)