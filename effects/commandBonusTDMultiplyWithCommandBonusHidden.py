#Item: Information Warfare Link - Electronic Superiority [Module]
type = "active", "gang"
def handler(fit, module, context):
    if context != "gang": return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for bonus in ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus")
        fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tracking Disruptor",
                                      bonus, module.getModifiedItemAttr("commandBonusTD") * mult,
                                      stackingPenalties = True)