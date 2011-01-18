#Used by:
#Implants named like: Hardwiring Zainou 'Deadeye' ZGS (6 of 6)
#Skill: Small Hybrid Turret
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
