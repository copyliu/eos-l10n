type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility",
                           module.getModifiedItemAttr("agilityMultiplier"),
                           stackingPenalties = True)