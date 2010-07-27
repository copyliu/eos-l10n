#Variations of item: Dominix (3 of 3) [Ship]
#Item: Rattlesnake [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Battleship").level
    for type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                     type, ship.getModifiedItemAttr("shipBonusGB2") * level)