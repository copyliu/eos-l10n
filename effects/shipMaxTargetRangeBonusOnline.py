#Used by:
#Modules from group: Signal Amplifier (11 of 11)
type = "passive"
def handler(fit, ship, context):
    fit.ship.boostItemAttr("maxTargetRange", ship.getModifiedItemAttr("maxTargetRangeBonus"),
                              stackingPenalties = True)
