#Used by:
#Ship: Myrmidon
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Battlecruisers").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                 "damageMultiplier", ship.getModifiedItemAttr("shipBonusBC1") * level)