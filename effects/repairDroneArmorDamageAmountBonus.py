#Variations of item: Large Drone Repair Augmentor I (2 of 2) [Module]
#Variations of item: Medium Drone Repair Augmentor I (2 of 2) [Module]
#Variations of item: Small Drone Repair Augmentor I (2 of 2) [Module]
#Item: Repair Drone Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Logistic Drone",
                                 "armorDamageAmount", container.getModifiedItemAttr("damageHP") * level)