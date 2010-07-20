#Item: Drone Navigation Computer I [Module]
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: True, "maxVelocity",
                                 module.getModifiedItemAttr("speedBoostFactor"))