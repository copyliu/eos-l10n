#Item: Hardwiring - Eifyr and Co. 'Gunslinger' LX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' LX-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' LX-2 [Implant]
#Item: Large Projectile Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
    