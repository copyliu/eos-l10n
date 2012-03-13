# Used by:
# Implants named like: Inherent Implants 'Noble' Repair Proficiency RP (6 of 6)
# Modules named like: Auxiliary Nano Pump (6 of 6)
# Modules named like: QA Multiship Module Players (4 of 4)
# Implant: Imperial Navy Modified 'Noble' Implant
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", implant.getModifiedItemAttr("repairBonus"),
                                  stackingPenalties = "implant" not in context)
