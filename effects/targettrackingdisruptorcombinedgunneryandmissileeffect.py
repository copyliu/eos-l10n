# Used by:
# Module: Tracking Disruptor I
type= "projected", "active"
def handler(fit, module, context):
    if "projected" in context:
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "trackingSpeed", module.getModifiedItemAttr("trackingSpeedBonus"),
                                      stackingPenalties = True)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "maxRange", module.getModifiedItemAttr("maxRangeBonus"),
                                      stackingPenalties = True)
        fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                      "falloff", module.getModifiedItemAttr("falloffBonus"),
                                      stackingPenalties = True)
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                        "aoeCloudSize", module.getModifiedItemAttr("aoeCloudSizeBonus"),
                                        stackingPenalties = True)
