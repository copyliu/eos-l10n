#Used by:
#Skills from group: Drones (6 of 19)
#Skills named like: Drone Specialization (4 of 4)
type = "passive"
def handler(fit, skill, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill(skill),
                                 "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)