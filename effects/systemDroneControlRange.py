#Items with name like: Black Hole Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    amount = beacon.getModifiedItemAttr("droneRangeMultiplier")
    fit.extraAttributes["droneControlRange"].multiply(amount)