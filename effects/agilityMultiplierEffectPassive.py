#Items with name like: Polycarbon Engine Housing (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility", module.getItemAttr("agilityMultiplier"), stackingPenalties = True)
