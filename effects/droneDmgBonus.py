#Items from group: Drones (6 of 19) [Skill]
#Items with name like: Drone Specialization (4 of 4)
type = "passive"
def handler(fit, skill, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill(skill),
                                 "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)