#Item: Hardwiring - Zainou 'Deadeye' ZGS10 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGS100 [Implant]
#Item: Hardwiring - Zainou 'Deadeye' ZGS1000 [Implant]
#Item: Small Hybrid Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
