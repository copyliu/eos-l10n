#Used by:
#Implants named like: Hardwiring Zainou 'Gypsy' KOB (6 of 6)
#Modules named like: Signal Disruption Amplifier (6 of 6)
#Skill: Electronic Warfare
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM Burst",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
