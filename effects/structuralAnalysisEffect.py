#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Armor Implants (3 of 3)
#Variations of item: Large Auxiliary Nano Pump I (2 of 2) [Module]
#Variations of item: Medium Auxiliary Nano Pump I (2 of 2) [Module]
#Variations of item: Small Auxiliary Nano Pump I (2 of 2) [Module]
#Item: Imperial Navy Modified 'Noble' Implant [Implant]
from customEffects import boostModListByReq
def structuralAnalysisEffect(self, fitting, state = None):
    boostModListByReq(fitting.modules, "armorDamageAmount", "repairBonus",
                      lambda mod: mod.group.name == "Armor Repair Unit",
                      self.item, useStackingPenalty = True)