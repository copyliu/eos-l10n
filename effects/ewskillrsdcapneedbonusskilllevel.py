# Used by:
# Implants named like: Hardwiring Zainou 'Gypsy' KRB (6 of 6)
# Skill: Sensor Linking
type = "passive"
def handler(fit, container, context):
    groups = ("Remote Sensor Damper", "Remote Sensor Booster")
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name in groups,
                                  "capacitorNeed", container.getModifiedItemAttr("capNeedBonus") * level)
