#Used by: Ship: Bantam
#               Tormentor
#               Navitas
#               Burst
from customEffects import boostModListByReq, multiply
def miningCapBonus(self, fitting):
    boostModListByReq(fitting.modules, "capacitorNeed", "capacitorNeedMultiplier",
                      lambda mod: mod.group.name == "Mining Laser", 
                      self.item, helper = multiply)