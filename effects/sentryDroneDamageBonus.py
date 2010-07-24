#Variations of item: Large Sentry Damage Augmentor I (2 of 2) [Module]
#Variations of item: Medium Sentry Damage Augmentor I (2 of 2) [Module]
#Variations of item: Small Sentry Damage Augmentor I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Sentry Drone Interfacing"),
                                 "damageMultiplier", module.getModifiedItemAttr("damageMultiplierBonus"),
                                 stackingPenalties = True)