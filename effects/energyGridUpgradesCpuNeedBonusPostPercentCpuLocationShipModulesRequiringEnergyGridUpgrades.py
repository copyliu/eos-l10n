#Items from group: Rig Energy Grid (6 of 30) [Module]
#Item: Energy Grid Upgrades [Skill]
#Item: Hardwiring - Inherent Implants 'Squire' GU2 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' GU4 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' GU8 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Grid Upgrades"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus") * level)