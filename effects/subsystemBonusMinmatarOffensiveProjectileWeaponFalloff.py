#Item: Loki Offensive - Projectile Scoping Array [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "falloff", module.getModifiedItemAttr("subsystemBonusMinmatarOffensive") * level)