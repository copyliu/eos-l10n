# Used by:
# Modules from group: Energy Transfer Array (38 of 38)
type = "projected", "active"
def handler(fit, module, context):
    if "projected" in context and not fit.ship.getModifiedItemAttr("disallowAssistance") == 1:
        amount = module.getModifiedItemAttr("powerTransferAmount")
        duration = module.getModifiedItemAttr("duration")
        fit.addDrain(duration, -amount, 0)
