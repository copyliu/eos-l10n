# Used by:
# Module: Information Warfare Link - Electronic Superiority
type = "active", "gang"
def handler(fit, module, context):
    if "gang" not in context: return
    mult = module.getModifiedItemAttr("commandBonusHidden")
    for bonus in ("maxRangeBonus", "falloffBonus", "trackingSpeedBonus"):
        fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tracking Disruptor",
                                      bonus, module.getModifiedItemAttr("commandBonusTD") * mult,
                                      stackingPenalties = True)
