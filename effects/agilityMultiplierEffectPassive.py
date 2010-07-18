type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility", module.getItemAttr("agilityMultiplier"), stackingPenalties = True)