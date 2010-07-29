#Item: Hardwiring - Inherent Implants 'Highwall' HY-0 [Implant]
#Item: Hardwiring - Inherent Implants 'Highwall' HY-1 [Implant]
#Item: Hardwiring - Inherent Implants 'Highwall' HY-2 [Implant]
#Item: Mining Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining Upgrades"),
                                  "cpuPenaltyPercent", container.getModifiedItemAttr("miningUpgradeCPUReductionBonus") * level)
