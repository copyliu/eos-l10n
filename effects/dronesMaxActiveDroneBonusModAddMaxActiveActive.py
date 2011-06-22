# Used by:
# Module: Drone Control Unit I
type = "active"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("maxActiveDroneBonus")
    fit.extraAttributes.increase("maxActiveDrones", amount)
