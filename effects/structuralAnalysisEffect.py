#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Armor Implants (3 of 3)
#Variations of item: Large Auxiliary Nano Pump I (2 of 2) [Module]
#Variations of item: Medium Auxiliary Nano Pump I (2 of 2) [Module]
#Variations of item: Small Auxiliary Nano Pump I (2 of 2) [Module]
#Item: Imperial Navy Modified 'Noble' Implant [Implant]
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", implant.getModifiedItemAttr("repairBonus"),
                                  stackingPenalties = "implant" not in context)
