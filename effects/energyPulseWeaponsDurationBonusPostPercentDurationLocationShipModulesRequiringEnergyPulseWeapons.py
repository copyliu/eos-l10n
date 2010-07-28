#Item: Energy Pulse Weapons [Skill]
#Item: Hardwiring - Inherent Implants 'Squire' EP2 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EP4 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EP8 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Pulse Weapons"),
                                  "duration", container.getModifiedItemAttr("durationBonus") * level)