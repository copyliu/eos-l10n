#Items from category: Charge (556 of 814)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("maxRange", module.getModifiedChargeAttr("weaponRangeMultiplier"))