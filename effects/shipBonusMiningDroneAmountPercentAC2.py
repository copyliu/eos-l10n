#Used by:
#Ship: Arbitrator
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Cruiser").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Combat Drone",
                                 "miningAmount", ship.Mining("shipBonusAC2") * level)