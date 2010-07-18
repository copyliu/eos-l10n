#Items from market group: Implants & Boosters > Booster (6 of 32)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("capacitorCapacity", booster.getModifiedItemAttr("boosterCapacitorCapacityPenalty"))