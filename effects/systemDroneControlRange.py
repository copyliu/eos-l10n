#Items from group: Effect Beacon (6 of 38) [Celestial]
type = "projected"
runTime = "late"
def handler(fit, beacon, context):
    fit.droneControlRange *= beacon.getModifiedItemAttr("droneRangeMultiplier")