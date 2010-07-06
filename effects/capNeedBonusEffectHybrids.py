#Used by: Item: Hybrid Discharge Elutriation
from customEffects import boostModListByReq
def capNeedBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item)