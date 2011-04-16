#Used by:
#Module: Drone Navigation Computer I
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), "maxVelocity",
                                 module.getModifiedItemAttr("speedBoostFactor"))
