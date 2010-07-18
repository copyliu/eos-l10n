type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("maxVelocity", booster.getModifiedItemAttr("boosterMaxVelocityPenalty"))