#Used by:
#Variations of ship: Dominix (3 of 3)
#Ship: Rattlesnake
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                 "damageMultiplier", ship.getModifiedItemAttr("shipBonusGB2") * level)