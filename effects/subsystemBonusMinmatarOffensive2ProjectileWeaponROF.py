#Item: Loki Offensive - Hardpoint Efficiency Configuration [Subsystem]
#Item: Loki Offensive - Projectile Scoping Array [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "speed", module.getModifiedItemAttr("subsystemBonusMinmatarOffensive2") * level)