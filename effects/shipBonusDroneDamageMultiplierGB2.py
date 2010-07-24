#Variations of item: Dominix (3 of 3) [Ship]
#Item: Rattlesnake [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    fit.drones.filteredItemBoost(lambda drone: drone.group.name == "Combat Drone",
                                 "damageMultiplier", ship.getModifiedItemAttr("shipBonusGB2") * level)