#Used by: Item: Auxiliary Nano Pump
from customEffects import boostModListByReq
def structuralAnalysisEffect(self, fitting, state = None):
    boostModListByReq(fitting.modules, "armorDamageAmount", "repairBonus",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, useStackingPenalty = True)