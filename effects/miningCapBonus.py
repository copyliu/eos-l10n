#Items from group: Frigate (4 of 35)
from customEffects import boostModListByReq, multiply
def miningCapBonus(self, fitting):
    boostModListByReq(fitting.modules, "capacitorNeed", "capacitorNeedMultiplier",
                      lambda mod: mod.group.name == "Mining Laser", 
                      self.item, helper = multiply)