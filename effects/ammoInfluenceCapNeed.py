#Used by:
#Items from category: Charge (461 of 814)
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("capacitorNeed", module.getModifiedChargeAttr("capNeedBonus"))