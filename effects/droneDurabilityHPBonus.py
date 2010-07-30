#Used by:
#Modules named like: Drone Durability Enhancer (6 of 6)
#Skill: Drone Durability
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "hp", container.getModifiedItemAttr("hullHpBonus") * level)
