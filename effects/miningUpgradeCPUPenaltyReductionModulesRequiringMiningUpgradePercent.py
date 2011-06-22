# Used by:
# Implants named like: Hardwiring Inherent Implants 'Highwall' HY (3 of 3)
# Skill: Mining Upgrades
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining Upgrades"),
                                  "cpuPenaltyPercent", container.getModifiedItemAttr("miningUpgradeCPUReductionBonus") * level)
