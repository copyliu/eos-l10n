# Used by:
# Implants from group: Booster (12 of 35)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("shieldCapacity", booster.getModifiedItemAttr("boosterShieldCapacityPenalty"))
