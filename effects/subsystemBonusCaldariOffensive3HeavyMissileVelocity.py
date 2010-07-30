#Item: Tengu Offensive - Accelerated Ejection Bay [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "maxVelocity", module.getModifiedItemAttr("subsystemBonusCaldariOffensive3") * level)
