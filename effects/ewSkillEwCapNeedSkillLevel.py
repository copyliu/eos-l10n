#Items from group: Rig Electronics (6 of 30) [Module]
#Item: Electronic Warfare [Skill]
#Item: Hardwiring - Zainou 'Gypsy' KOB-25 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KOB-50 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KOB-75 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "ECM",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)