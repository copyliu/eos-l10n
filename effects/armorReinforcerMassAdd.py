type = "passive"
def handler(fit, module, context):
    fit.ship.increaseItemAttr("mass", module.getModifiedItemAttr("massAddition"))