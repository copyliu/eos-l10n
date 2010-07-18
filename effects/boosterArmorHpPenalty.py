#Items from market group: Implants & Boosters > Booster (12 of 32)
type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("armorHP", booster.getModifiedItemAttr("boosterArmorHPPenalty"))