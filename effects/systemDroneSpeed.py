#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    fit.drones.filteredItemMultiply(lambda drone: True,
                                    "maxVelocity", beacon.getModifiedItemAttr("maxDroneVelocityMultiplier"))