#Used by:
#Modules named like: Drone Speed Augmentor (6 of 6)
#Skill: Drone Navigation
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "maxVelocity", container.getModifiedItemAttr("droneMaxVelocityBonus") * level)
