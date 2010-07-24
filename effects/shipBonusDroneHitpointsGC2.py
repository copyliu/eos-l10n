#Variations of item: Vexor (3 of 4) [Ship]
#Item: Gila [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    for type in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.group.name == "Combat Drone",
                                     type, ship.getModifiedItemAttr("shipBonusGC2") * level)