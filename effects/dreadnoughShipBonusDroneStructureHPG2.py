#Used by:
#Ship: Moros
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Dreadnought").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                "hp", ship.getModifiedItemAttr("dreadnoughtShipBonusG2") * level)
