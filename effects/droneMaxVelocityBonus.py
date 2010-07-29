#Variations of item: Large Drone Speed Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Speed Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Speed Augmentor I (2 of 2) [Module]
#Item: Drone Navigation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "maxVelocity", container.getModifiedItemAttr("droneMaxVelocityBonus") * level)
