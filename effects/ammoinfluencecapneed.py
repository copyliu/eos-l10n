# Used by:
# Items from category: Charge (453 of 816)
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("capacitorNeed", module.getModifiedChargeAttr("capNeedBonus") or 0)
