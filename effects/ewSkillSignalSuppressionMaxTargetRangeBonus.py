#Items with name like: Inverted Signal Field Projector (6 of 6)
#Item: Signal Suppression [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "maxTargetRangeBonus", container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level)
