# Used by:
# Modules from group: Drone Navigation Computer (2 of 2)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Mining Drone Operation"), "maxVelocity",
                                 module.getModifiedItemAttr("speedBoostFactor"), stackingPenalties = True)
