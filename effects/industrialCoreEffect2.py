#Item: Industrial Core I [Module]
type = "active"
def handler(fit, module, context):
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"))
    fit.ship.multiplyItemAttr("mass", module.getModifiedItemAttr("massMultiplier"))