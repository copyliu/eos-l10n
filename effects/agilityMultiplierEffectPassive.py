# Used by:
# Modules named like: Polycarbon Engine Housing (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("agilityMultiplier"), stackingPenalties = True)
