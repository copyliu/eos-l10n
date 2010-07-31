#Used by:
#Implants named like: Hardwiring Zainou 'Gypsy' KRB (3 of 3)
#Skill: Sensor Linking
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
