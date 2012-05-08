# Used by:
# Module: Tracking Disruptor II
type= "projected", "active"
def handler(fit, module, context):
    if "projected" in context:
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                        "aoeCloudSize", module.getModifiedItemAttr("aoeCloudSizeBonus"),
                                        stackingPenalties = True)
