#Used by:
#Modules named like: Auxiliary Nano Pump (6 of 6)
#Implant: Hardwiring - Inherent Implants 'Noble' ZET40
#Implant: Hardwiring - Inherent Implants 'Noble' ZET400
#Implant: Hardwiring - Inherent Implants 'Noble' ZET4000
#Implant: Imperial Navy Modified 'Noble' Implant
type = "passive"
def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", implant.getModifiedItemAttr("repairBonus"),
                                  stackingPenalties = "implant" not in context)
