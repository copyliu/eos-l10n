#Used by:
#Implants named like: Hardwiring Inherent Implants 'Lancer' Gamma (3 of 3)
#Skill: Medium Energy Turret
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
