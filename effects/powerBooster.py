#Used by:
#Modules from group: Capacitor Booster (54 of 54)
type = "active"
def handler(fit, module, context):
    if module.charge is None: return
    capAmount = module.getModifiedChargeAttr("capacitorBonus") or 0
    module.itemModifiedAttributes["capacitorNeed"] = -capAmount
