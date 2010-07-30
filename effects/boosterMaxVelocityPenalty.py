#Items from group: Booster (12 of 34) [Implant]
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("maxVelocity", booster.getModifiedItemAttr("boosterMaxVelocityPenalty"))