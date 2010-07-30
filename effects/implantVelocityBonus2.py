#Item: Republic Special Ops Field Enhancer - Gamma [Implant]
type = "passive"
def handler(fit, implant, context):
    fit.ship.boostItemAttr("maxVelocity", implant.getModifiedItemAttr("velocityBonus2"))