#Item: Vexor [Ship]
#Item: Vexor Navy Issue [Ship]
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.drones.filteredItemBoost(lambda drone: drone.group.name == "Mining Drone",
                                 "miningAmount", ship.Mining("shipBonusGC2") * level)