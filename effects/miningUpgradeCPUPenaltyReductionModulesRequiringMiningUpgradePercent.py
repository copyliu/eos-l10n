#Items with name like: Hardwiring - Inherent Implants 'Highwall' (3 of 6)
#Item: Mining Upgrades [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining Upgrades"),
                                  "cpuPenaltyPercent", container.getModifiedItemAttr("miningUpgradeCPUReductionBonus") * level)
