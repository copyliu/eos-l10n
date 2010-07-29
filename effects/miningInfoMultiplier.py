#Items from group: Mining Crystal (30 of 30) [Charge]
#Items with name like: Mining Crystal (32 of 32)
type = "passive"
def handler(fit, module, context):
    module.multiplyItemAttr("miningAmount", module.getModifiedChargeAttr("specialisationAsteroidYieldMultiplier"))