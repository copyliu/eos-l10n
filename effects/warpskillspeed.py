# Used by:
# Implants named like: Eifyr and Co. 'Rogue' Warp Drive Speed WS (6 of 6)
# Modules named like: Hyperspatial Velocity Optimizer (6 of 6)
type = "passive"
def handler(fit, container, context):
    fit.ship.boostItemAttr("baseWarpSpeed", container.getModifiedItemAttr("WarpSBonus"))
