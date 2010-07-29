#Variations of item: Large Drone Mining Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Mining Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Mining Augmentor I (2 of 2) [Module]
#Item: Drone Interfacing [Skill]
#Item: Mining Drone Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Mining Drone",
                                 "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level,
                                 stackingPenalties = "skill" not in context)
