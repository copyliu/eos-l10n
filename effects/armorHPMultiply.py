type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("armorHP", module.getModifiedItemAttr("armorHPMultiplier"))