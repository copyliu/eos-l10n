#Used by:
#Implants named like: Hardwiring Inherent Implants 'Lancer' Epsilon (3 of 3)
#Implant: Pashan's Turret Handling Mindlink
#Skill: Large Energy Turret
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
