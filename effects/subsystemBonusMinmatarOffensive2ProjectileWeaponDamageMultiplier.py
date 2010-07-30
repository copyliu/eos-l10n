#Item: Loki Offensive - Turret Concurrence Registry [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", module.getModifiedItemAttr("subsystemBonusMinmatarOffensive2") * level)
