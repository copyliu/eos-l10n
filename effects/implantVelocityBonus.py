#Used by:
#Implants named like: Hardwiring Eifyr and Co. 'Rogue' CY (3 of 3)
#Implant: Shaqil's Speed Enhancer
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("maxVelocity", implant.getModifiedItemAttr("implantBonusVelocity"))