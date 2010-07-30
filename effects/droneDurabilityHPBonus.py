#Items with name like: Drone Durability (7 of 7)
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "hp", container.getModifiedItemAttr("hullHpBonus") * level)
