#Item: Hardwiring - Inherent Implants 'Lancer' G0-Gamma [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G1-Gamma [Implant]
#Item: Hardwiring - Inherent Implants 'Lancer' G2-Gamma [Implant]
#Item: Medium Energy Turret [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                  "damageMultiplier", container.getModifiedItemAttr("damageMultiplierBonus") * level)