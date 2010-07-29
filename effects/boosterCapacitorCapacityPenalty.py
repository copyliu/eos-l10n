#Items with name like: Blue Pill Booster (3 of 5)
#Items with name like: Exile Booster (3 of 4)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("capacitorCapacity", booster.getModifiedItemAttr("boosterCapacitorCapacityPenalty"))