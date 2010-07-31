#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Gunslinger' SX (3 of 3)
#Skill: Small Projectile Turret
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
