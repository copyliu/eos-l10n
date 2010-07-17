type = "passive"
def handler(fit, module, context):
    module.multipleItemAttr("falloff", module.getModifiedChargeAttr("fallofMultiplier"))