#Used by: Item: Energy Discharge Elutriation
from customEffects import boostModListByReq
def capNeedBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)