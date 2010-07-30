#Used by:
#Modules named like: Sentry Damage Augmentor (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Sentry Drone Interfacing"),
                                 "damageMultiplier", module.getModifiedItemAttr("damageMultiplierBonus"),
                                 stackingPenalties = True)