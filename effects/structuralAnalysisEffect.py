#Items from group: Cyber Armor (4 of 24)
#Items from group: Rig Armor (6 of 54)
from customEffects import boostModListByReq
def structuralAnalysisEffect(self, fitting, state = None):
    boostModListByReq(fitting.modules, "armorDamageAmount", "repairBonus",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, useStackingPenalty = True)