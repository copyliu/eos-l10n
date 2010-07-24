#Variations of item: Arbitrator (3 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    for type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.group.name == "Combat Drone",
                                     type, ship.getModifiedItemAttr("shipBonusAC2") * level)