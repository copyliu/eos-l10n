# Used by:
# Celestials named like: Magnetar Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.drones.filteredItemMultiply(lambda drone: drone.item.group.name == "Combat Drone",
                                    "damageMultiplier", beacon.getModifiedItemAttr("damageMultiplierMultiplier"))