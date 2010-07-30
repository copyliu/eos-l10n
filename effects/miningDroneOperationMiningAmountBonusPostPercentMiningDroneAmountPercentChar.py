#Used by:
#Modules named like: Drone Mining Augmentor (6 of 6)
#Skill: Drone Interfacing
#Skill: Mining Drone Operation
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Mining Drone",
                                 "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level,
                                 stackingPenalties = "skill" not in context)
