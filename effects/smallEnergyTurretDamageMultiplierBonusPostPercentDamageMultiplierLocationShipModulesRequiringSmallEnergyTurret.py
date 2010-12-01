#Used by:
#Implants named like: Hardwiring Inherent Implants 'Lancer' Alpha (3 of 3)
#Skill: Small Energy Turret
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
