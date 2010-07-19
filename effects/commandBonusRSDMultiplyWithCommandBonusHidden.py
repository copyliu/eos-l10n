#Item: Information Warfare Link - Electronic Superiority [Module]
type = "active", "gang"
def handler(fit, module, context):
    if context != "gang": return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for bonus in ("scanResolutionBonus", "maxTargetRangeBonus"):
        fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Remote Sensor Damper",
                                      bonus, module.getModifiedItemAttr("commandBonusRSD") * mult,
                                      stackingPenalties = True)