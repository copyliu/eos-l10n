#Used by:
#Module: Industrial Core I
type = "active"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"))
    fit.ship.multiplyItemAttr("mass", module.getModifiedItemAttr("massMultiplier"))