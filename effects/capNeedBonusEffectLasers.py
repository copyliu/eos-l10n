#Variations of item: Large Energy Discharge Elutriation I (2 of 2)
#Variations of item: Medium Energy Discharge Elutriation I (2 of 2)
#Variations of item: Small Energy Discharge Elutriation I (2 of 2)
from customEffects import boostModListByReq
def capNeedBonusEffectLasers(self, fitting, state):
    boostModListByReq(fitting.modules, "capacitorNeed", "capNeedBonus",
                      lambda mod: mod.group.name == "Energy Weapon", self.item)