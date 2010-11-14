#Used by:
#Module: Armored Warfare Link - Rapid Repair
type = "gang", "active"
gangBoost = "armorRepairDuration"
def handler(fit, module, context):
    if "gang" not in context: return
    groups = ("Armor Repair Unit", "Armor Repair Projector")
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "duration", module.getModifiedItemAttr("commandBonus"),
                                  stackingPenalties = True)
