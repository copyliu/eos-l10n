#Item: Moros [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Dreadnought").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                 "damageMultiplier", ship.getModifiedItemAttr("dreadnoughtShipBonusG2") * level)