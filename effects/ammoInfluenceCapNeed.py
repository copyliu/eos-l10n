# Used by:
# Items from category: Charge (440 of 816)
# Charges from group: Frequency Crystal (184 of 184)
# Charges from group: Hybrid Ammo (208 of 208)
# Charges from group: Mining Crystal (30 of 30)
type = "passive"
def handler(fit, module, context):
    module.boostItemAttr("capacitorNeed", module.getModifiedChargeAttr("capNeedBonus") or 0)
