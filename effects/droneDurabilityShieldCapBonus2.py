#Used by:
#Skill: Drone Durability
type = "passive"
def handler(fit, skill, context):
    fit.drones.filteredDroneBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                  "shieldCapacity", skill.getModifiedItemAttr("shieldCapacityBonus") * skill.level)