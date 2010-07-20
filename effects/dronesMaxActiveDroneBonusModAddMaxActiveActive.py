#Item: Drone Control Unit I [Module]
type = "active"
def handler(fit, module, context):
    fit.maxActiveDrones += module.getModifiedItemAttr("maxActiveDroneBonus")