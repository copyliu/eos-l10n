type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("maxRange", module.getModifiedChargeAttr("weaponRangeMultiplier"))