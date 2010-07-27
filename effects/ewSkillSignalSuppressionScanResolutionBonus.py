#Variations of item: Large Inverted Signal Field Projector I (2 of 2) [Module]
#Variations of item: Medium Inverted Signal Field Projector I (2 of 2) [Module]
#Variations of item: Small Inverted Signal Field Projector I (2 of 2) [Module]
#Item: Signal Suppression [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Sensor Damper",
                                  "scanResolutionBonus", container.getModifiedItemAttr("scanSkillEwStrengthBonus") * level)