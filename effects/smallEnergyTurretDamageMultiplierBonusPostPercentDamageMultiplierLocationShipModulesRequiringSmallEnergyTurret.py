#Item: Hardwiring - Inherent Implants 'Lancer' G0-Alpha [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Alpha [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Alpha [Implant]
#Item: Small Energy Turret [Skill]
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)