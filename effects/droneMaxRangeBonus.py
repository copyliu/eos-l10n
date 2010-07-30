#Items with name like: Drone Scope Chip (6 of 6)
#Item: Drone Sharpshooting [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "maxRange", container.getModifiedItemAttr("rangeSkillBonus") * level)
