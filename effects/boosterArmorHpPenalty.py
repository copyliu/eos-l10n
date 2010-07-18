type = "boosterSideEffect"
def handler(fit, booster, context):
    fit.ship.boostItemAttr("armorHP", booster.getModifiedItemAttr("boosterArmorHPPenalty"))