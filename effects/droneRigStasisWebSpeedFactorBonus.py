#Variations of item: Large Stasis Drone Augmentor I (2 of 2) [Module]
#Variations of item: Medium Stasis Drone Augmentor I (2 of 2) [Module]
#Variations of item: Small Stasis Drone Augmentor I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Stasis Webifying Drone",
                                 "speedFactor", module.getModifiedItemAttr("webSpeedFactorBonus"))