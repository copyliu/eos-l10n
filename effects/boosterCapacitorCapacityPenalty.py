type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("capacitorCapacity", booster.getModifiedItemAttr("boosterCapacitorCapacityPenalty"))