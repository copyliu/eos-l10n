type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("capacitorNeed", module.getModifiedChargeAttr("capNeedBonus"))