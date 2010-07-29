#Items with name like: Cataclysmic Variable Effect Beacon Class (6 of 6)
#Items with name like: Pulsar Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("rechargeRate", beacon.getModifiedItemAttr("rechargeRateMultiplier"))