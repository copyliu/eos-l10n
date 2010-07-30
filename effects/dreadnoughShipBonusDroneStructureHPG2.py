#Item: Moros [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Dreadnought")
    fit.drones.filteredItemBoost(lambda drone: True, "hp",
                                 ship.getModifiedItemAttr("dreadnoughtShipBonusG2") * level)