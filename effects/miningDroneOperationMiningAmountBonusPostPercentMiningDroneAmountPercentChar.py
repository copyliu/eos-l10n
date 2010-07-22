#Variations of item: Large Drone Mining Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Mining Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Mining Augmentor I (2 of 2) [Module]
#Item: Drone Interfacing [Skill]
#Item: Mining Drone Operation [Skill]
type = "passive"
def handlr(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.drones.filteredItemBoost(lambda drone: drone.group.name == "Mining Drone",
                                 "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level,
                                 stackingPenalties = context != "skill")