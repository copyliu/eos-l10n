#Used by: Ship: Freki
from customEffects import boostModListByReq
def shipBonusAfterburnerCapNeedATF(self, fitting):
    boostModListByReq(fitting.modules, "capacitorNeed", "shipBonusATF1", 
                      lambda mod: mod.group.name == "Afterburner", self.item)