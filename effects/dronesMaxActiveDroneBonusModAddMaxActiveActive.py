#Item: Drone Control Unit I [Module]
type = "active"
def handler(fit, module, context):
    amount = module.getModifiedItemAttr("maxActiveDroneBonus")
    fit.extraAttributes["maxActiveDrones"].increase(amount)