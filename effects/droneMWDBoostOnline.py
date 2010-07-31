#Used by:
#Module: Drone Navigation Computer I
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: True, "maxVelocity",
                                 module.getModifiedItemAttr("speedBoostFactor"))