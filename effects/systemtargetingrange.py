# Used by:
# Celestials named like: Magnetar Effect Beacon Class (6 of 6)
# Celestials named like: Pulsar Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("maxTargetRange", beacon.getModifiedItemAttr("maxTargetRangeMultiplier"))