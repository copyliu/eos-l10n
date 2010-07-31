#Used by:
#Module: Information Warfare Link - Electronic Superiority
type = "active", "gang"
def handler(fit, module, context):
    if "gang" not in context: return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for bonus in ("scanResolutionBonus", "maxTargetRangeBonus"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                      bonus, module.getModifiedItemAttr("commandBonusRSD") * mult,
                                      stackingPenalties = True)
