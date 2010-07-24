#Variations of item: Arbitrator (3 of 3) [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.drones.filteredItemBoost(lambda drone: drone.group.name == "Combat Drone",
                                 "damageMultiplier", ship.getModifiedItemAttr("shipBonusAC2") * level)