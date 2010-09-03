#Used by:
#Modules from group: Capacitor Booster (54 of 54)
type = "active"
def handler(fit, module, context):
    if module.charge is None: return
    #This is quite the effect compared to most others.
    #So an explanation is probably at hand.

    #Step 1: We fetch all the attributes we'll need
    capAmount = module.getModifiedChargeAttr("capacitorBonus") or 0

    #Add the boost per second to the fit
    module.itemModifiedAttributes["capacitorNeed"] = -capAmount
