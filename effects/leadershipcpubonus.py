# Used by:
# Ships from group: Battlecruiser (9 of 12)
# Ships from group: Carrier (4 of 4)
# Ships from group: Command Ship (8 of 8)
# Ships from group: Supercarrier (5 of 5)
# Ships from group: Titan (4 of 4)
# Subsystems named like: Defensive Warfare Processor (4 of 4)
# Ship: Orca
# Ship: Rorqual
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Leadership"),
                                  "cpu", container.getModifiedItemAttr("cpuNeedBonus"))
