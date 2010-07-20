#Variations of item: Large Drone Scope Chip I (2 of 2) [Module]
#Variations of item: Medium Drone Scope Chip I (2 of 2) [Module]
#Variations of item: Small Drone Scope Chip I (2 of 2) [Module]
#Item: Drone Sharpshooting [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.skill if context == "skill" else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level)