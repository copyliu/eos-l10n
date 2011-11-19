# Used by:
# Celestials named like: Magnetar Effect Beacon Class (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, beacon, context):
    fit.drones.filteredItemMultiply(lambda drone: True,
                                    "damageMultiplier", beacon.getModifiedItemAttr("damageMultiplierMultiplier"))
