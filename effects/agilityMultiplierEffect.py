#Items from group: Inertia Stabilizer (12 of 12) [Module]
#Items from group: Nanofiber Internal Structure (14 of 14) [Module]
#Items from group: Reinforced Bulkhead (12 of 12) [Module]
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility",
                           module.getModifiedItemAttr("agilityMultiplier"),
                           stackingPenalties = True)