#Item: Hardwiring - Eifyr and Co. 'Gunslinger' SX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' SX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' SX-2 [Implant]
#Item: Small Projectile Turret [Skill]
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
