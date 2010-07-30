#Used by:
#Modules from group: Drone Tracking Modules (2 of 2)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemMultiply(lambda drone: "trackingSpeed" in drone.itemModifiedAttributes,
                                    "trackingSpeed", module.getModifiedItemAttr("trackingSpeedMultiplier"))
    fit.drones.filteredItemMultiply(lambda drone: "maxRange" in drone.itemModifiedAttributes,
                                    "maxRange", module.getModifiedItemAttr("maxRangeMultiplier"))