#Items from group: Effect Beacon (12 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("rechargeRate", beacon.getModifiedItemAttr("rechargeRateMultiplier"))