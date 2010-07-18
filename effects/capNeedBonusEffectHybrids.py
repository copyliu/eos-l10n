#Variations of item: Large Hybrid Discharge Elutriation I (2 of 2)
#Variations of item: Medium Hybrid Discharge Elutriation I (2 of 2)
#Variations of item: Small Hybrid Discharge Elutriation I (2 of 2)
from customEffects import boostModListByReq
def capNeedBonusEffectHybrids(self, fitting, state):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Hybrid Weapon", self.item)