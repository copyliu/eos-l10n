# Used by:
# Modules from group: Drone Navigation Computer (2 of 2)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"), "maxVelocity",
                                 module.getModifiedItemAttr("speedBoostFactor"), stackingPenalties = True)
