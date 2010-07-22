#Item: Hardwiring - Zainou 'Deadeye' ZGL10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGL100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGL1000 [Implant]
#Item: Large Hybrid Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)