#Variations of item: Large Drone Durability Enhancer I (2 of 2) [Module]
#Variations of item: Medium Drone Durability Enhancer I (2 of 2) [Module]
#Variations of item: Small Drone Durability Enhancer I (2 of 2) [Module]
#Item: Drone Durability [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "hp", container.getModifiedItemAttr("hullHpBonus") * level)
