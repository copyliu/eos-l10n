# Used by:
# Celestials named like: Black Hole Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("agility", beacon.getModifiedItemAttr("agilityMultiplier"))