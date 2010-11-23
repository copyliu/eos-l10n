#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Rogue' HY (6 of 6)
#Modules named like: Hyperspatial Velocity Optimizer (6 of 6)
type = "passive"
def handler(fit, container, context):
    fit.ship.boostItemAttr("baseWarpSpeed", container.getModifiedItemAttr("WarpSBonus"))
