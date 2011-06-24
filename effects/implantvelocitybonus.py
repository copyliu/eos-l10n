# Used by:
# Implants named like: Hardwiring Eifyr and Co. 'Rogue' CY (6 of 6)
# Implant: Shaqil's Speed Enhancer
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("maxVelocity", implant.getModifiedItemAttr("implantBonusVelocity"))