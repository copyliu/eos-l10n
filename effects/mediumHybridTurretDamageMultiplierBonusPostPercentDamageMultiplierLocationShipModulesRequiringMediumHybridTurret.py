#Item: Hardwiring - Zainou 'Deadeye' ZGM10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGM100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGM1000 [Implant]
#Item: Medium Hybrid Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)