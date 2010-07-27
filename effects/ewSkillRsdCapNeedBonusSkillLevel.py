#Item: Hardwiring - Zainou 'Gypsy' KRB-25 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KRB-50 [Implant]
#Item: Hardwiring - Zainou 'Gypsy' KRB-75 [Implant]
#Item: Sensor Linking [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)