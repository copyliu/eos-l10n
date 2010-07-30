#Items with name like: Vexor (2 of 2)
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Gallente Cruiser").level
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Mining Drone",
                                 "miningAmount", ship.Mining("shipBonusGC2") * level)