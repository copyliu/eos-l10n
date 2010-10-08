#Used by:
#Modules from group: Energy Vampire (52 of 52)
type = "active", "projected"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("powerTransferAmount")
    time = module.getModifiedItemAttr("duration") / 1000.0
    persec = amount / time
    if "projected" in context and fit.ship.getModifiedItemAttr("disallowOffensiveModifiers") != 1:
        fit.addDrain(time, amount, 0)
    elif "module" in context:
        module.itemModifiedAttributes["capacitorNeed"] = -amount
