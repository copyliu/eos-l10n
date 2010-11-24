#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Rogue' FY (6 of 6)
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("warpCapacitorNeed", implant.getModifiedItemAttr("warpCapacitorNeedBonus"))
