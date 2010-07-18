type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("trackingSpeed", module.getModifiedChargeAttr("trackingSpeedMultiplier"))