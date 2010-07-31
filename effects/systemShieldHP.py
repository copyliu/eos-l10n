#Used by:
#Celestials named like: Pulsar Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("shieldCapacity", beacon.getModifiedItemAttr("shieldCapacityMultiplier"))