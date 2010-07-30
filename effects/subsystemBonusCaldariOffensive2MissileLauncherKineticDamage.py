#Item: Tengu Offensive - Accelerated Ejection Bay [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "kineticDamage", module.getModifiedItemAttr("subsystemBonusCaldariOffensive2") * level)
