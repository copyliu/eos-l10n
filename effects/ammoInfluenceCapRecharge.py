type = "passive"
def handler(fit, module, context):
    fit.ship.multiplyItemAttr("rechargeRate", module.getModifiedChargeAttr("capacitorRechargeRateMultiplier"))