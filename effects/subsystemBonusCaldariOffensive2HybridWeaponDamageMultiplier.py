#Item: Tengu Offensive - Magnetic Infusion Basin [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", module.getModifiedItemAttr("subsystemBonusCaldariOffensive2") * level)