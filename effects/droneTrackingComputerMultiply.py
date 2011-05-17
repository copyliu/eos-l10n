#Used by:
#Modules from group: Drone Tracking Modules (2 of 2)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemMultiply(lambda drone: drone.item.requiresSkill("Drones"),
                                    "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"),
                                    stackingPenalties = True
                                    )
    fit.drones.filteredItemMultiply(lambda drone: drone.item.requiresSkill("Drones"),
                                    "maxRange", module.getModifiedItemAttr("maxRangeMultiplier"),
                                    stackingPenalties = True
                                    )
