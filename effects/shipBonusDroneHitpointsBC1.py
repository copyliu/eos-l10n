#Used by:
#Ship: Myrmidon
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    for layer in ("shieldCapacity", "armorHP", "hp"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     layer, ship.getModifiedItemAttr("shipBonusBC1") * level)
