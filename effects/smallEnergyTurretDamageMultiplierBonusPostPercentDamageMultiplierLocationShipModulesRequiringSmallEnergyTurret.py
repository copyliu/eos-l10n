#Item: Hardwiring - Inherent Implants 'Lancer' G0-Alpha [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Alpha [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Alpha [Implant]
#Item: Small Energy Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)
