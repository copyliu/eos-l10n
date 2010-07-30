#Items with name like: Signal Disruption Amplifier (6 of 6)
#Item: Electronic Warfare [Skill]
#Item: Hardwiring - Zainou 'Gypsy' KOB-25 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KOB-50 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KOB-75 [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
