#Items from group: Energy Transfer Array (37 of 37) [Module]
type = "projected", "active"
def handler(fit, module, context):
    if "projected" not in context: return
    amount = module.getModifiedItemAttr("powerTransferAmount")
    duration = module.getModifiedItemAttr("duration") / 1000.0
    fit.extraAttributes["capBoost"].increase(amount / duration)
