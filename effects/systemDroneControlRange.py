#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
def handler(fit, beacon, context):
    amount = beacon.getModifiedItemAttr("droneRangeMultiplier")
    fit.extraAttributes["droneControlRange"].multiply(amount)