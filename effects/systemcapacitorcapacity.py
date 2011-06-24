# Used by:
# Celestials named like: Cataclysmic Variable Effect Beacon Class (6 of 6)
type = "projected"
def handler(fit, beacon, context):
    fit.ship.multiplyItemAttr("capacitorCapacity", beacon.getModifiedItemAttr("capacitorCapacityMultiplierSystem"))