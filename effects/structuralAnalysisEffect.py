#Used by:
#Modules named like: Auxiliary Nano Pump (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 9 > Armor Implants (6 of 6)
#Implant: Imperial Navy Modified 'Noble' Implant
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", implant.getModifiedItemAttr("repairBonus"),
                                  stackingPenalties = "implant" not in context)
