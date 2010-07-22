#Item: Hardwiring - Inherent Implants 'Lancer' G0-Epsilon [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Epsilon [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Epsilon [Implant]
#Item: Large Energy Turret [Skill]
#Item: Pashan's Turret Handling Mindlink [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)