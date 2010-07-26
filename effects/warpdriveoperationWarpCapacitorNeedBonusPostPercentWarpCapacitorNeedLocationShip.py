#Item: Hardwiring - Eifyr and Co. 'Rogue' FY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' FY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' FY-2 [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("warpCapacitorNeed", implant.getModifiedItemAttr("warpCapacitorNeedBonus"))