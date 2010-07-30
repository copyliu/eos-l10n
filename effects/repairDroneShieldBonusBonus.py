#Items with name like: Drone Repair Augmentor (6 of 6)
#Item: Repair Drone Operation [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Logistic Drone",
                                 "shieldBonus", container.getModifiedItemAttr("damageHP") * level)
