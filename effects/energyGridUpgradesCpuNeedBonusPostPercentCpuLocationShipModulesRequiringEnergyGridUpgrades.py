# Used by:
# Implants named like: Hardwiring Inherent Implants 'Squire' GU (6 of 6)
# Modules named like: Powergrid Subroutine Maximizer (6 of 6)
# Skill: Energy Grid Upgrades
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Energy Grid Upgrades"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus") * level)
