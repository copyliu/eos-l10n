#Used by:
#Modules from group: Energy Transfer Array (37 of 37)
type = "projected", "active"
def handler(fit, module, context):
    if "projected" not in context: return
    amount = module.getModifiedItemAttr("powerTransferAmount")
    duration = module.getModifiedItemAttr("duration") / 1000.0
    fit.addDrain(duration, -amount, 0)
