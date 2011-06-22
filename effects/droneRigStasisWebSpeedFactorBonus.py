# Used by:
# Modules named like: Stasis Drone Augmentor (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.group.name == "Stasis Webifying Drone",
                                 "speedFactor", module.getModifiedItemAttr("webSpeedFactorBonus"))