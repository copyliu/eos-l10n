#Item: Hardwiring - Eifyr and Co 'Gunslinger' MX-2 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' MX-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Gunslinger' MX-1 [Implant]
#Item: Medium Projectile Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
