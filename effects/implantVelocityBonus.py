#Item: Hardwiring - Eifyr and Co. 'Rogue' CY-0 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' CY-1 [Implant]
#Item: Hardwiring - Eifyr and Co. 'Rogue' CY-2 [Implant]
#Item: Shaqil's Speed Enhancer [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("maxVelocity", implant.getModifiedItemAttr("implantBonusVelocity"))