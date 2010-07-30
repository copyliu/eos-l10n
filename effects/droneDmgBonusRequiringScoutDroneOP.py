#Item: Combat Drone Operation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Scout Drone Operation"),
                                 "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)