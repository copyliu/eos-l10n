#Items from group: Rig Energy Grid (6 of 30) [Module]
#Item: Energy Emission Systems [Skill]
#Item: Hardwiring - Inherent Implants 'Squire' EE2 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EE4 [Implant]
#Item: Hardwiring - Inherent Implants 'Squire' EE8 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Emission Systems"),
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
