# Used by:
# Variations of module: Information Warfare Link - Electronic Superiority I (2 of 2)
type = "active", "gang"
def handler(fit, module, context):
    if "gang" not in context: return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for bonus in ("scanResolutionBonus", "maxTargetRangeBonus"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                      bonus, module.getModifiedItemAttr("commandBonusRSD") * mult,
                                      stackingPenalties = True)
