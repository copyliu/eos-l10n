#Items from group: Signal Amplifier (11 of 11) [Module]
type = "passive"
def handler(fit, ship, context):
    fit.ship.boostItemAttr("scanResolution", ship.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties = True)