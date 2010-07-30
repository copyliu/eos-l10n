#Items with name like: Hyperspatial Velocity Optimizer (6 of 6)
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-2 [Implant]
type = "passive"
def handler(fit, container, context):
    fit.ship.boostItemAttr("baseWarpSpeed", container.getModifiedItemAttr("WarpSBonus"))
