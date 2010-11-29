#Used by:
#Implants named like: Hardwiring Zainou 'Deadeye' ZGM (3 of 3)
#Skill: Medium Hybrid Turret
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
