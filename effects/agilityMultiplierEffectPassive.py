#Variations of item: Large Polycarbon Engine Housing I (2 of 2)
#Variations of item: Medium Polycarbon Engine Housing I (2 of 2)
#Variations of item: Small Polycarbon Engine Housing I (2 of 2)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility", module.getItemAttr("agilityMultiplier"), stackingPenalties = True)