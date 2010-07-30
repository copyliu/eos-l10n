#Items from group: Energy Vampire (52 of 52) [Module]
type = "active", "projected"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("powerTransferAmount")
    time = module.getModifiedItemAttr("duration") / 1000.0
    persec = amount / time
    if "projected" in context and fit.ship.getModifiedItemAttr("disallowOffensiveModifiers") != 1:
        fit.extraAttributes["capDrain"].increase(persec)
    elif "module" in context:
        fit.extraAttributes["capBoost"].increase(persec)
