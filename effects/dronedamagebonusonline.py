# Used by:
# Modules from group: Drone Damage Modules (2 of 2)
type = "passive"
def handler(fit, module, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                 "damageMultiplier", module.getModifiedItemAttr("droneDamageBonus"),
                                 stackingPenalties = True)
