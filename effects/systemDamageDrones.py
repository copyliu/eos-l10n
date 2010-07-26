#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    fit.drones.filteredItemMultiply(lambda drone: drone.group.name == "Combat Drone",
                                    "damageMultiplier", beacon.getModifiedItemAttr("damageMultiplierMultiplier"))