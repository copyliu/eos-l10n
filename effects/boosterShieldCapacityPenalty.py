type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("shieldCapacity", booster.getModifiedItemAttr("boosterShieldCapacityPenalty"))