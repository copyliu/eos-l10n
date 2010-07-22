#Items from group: Mining Crystal (30 of 30) [Charge]
#Items from market group: Ammunition & Charges > Mining Crystals (32 of 32)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("miningAmount", module.getModifiedChargeAttr("specialisationAsteroidYieldMultiplier"))