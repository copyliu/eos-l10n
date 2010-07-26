#Variations of item: Large Hyperspatial Velocity Optimizer I (2 of 2) [Module]
#Variations of item: Medium Hyperspatial Velocity Optimizer I (2 of 2) [Module]
#Variations of item: Small Hyperspatial Velocity Optimizer I (2 of 2) [Module]
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' HY-2 [Implant]
def handler(fit, container, context):
    fit.ship.boostItemAttr("baseWarpSpeed", container.getModifiedItemAttr("WarpSBonus"))