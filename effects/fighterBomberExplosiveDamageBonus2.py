#Item: Fighter Bombers [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Fighter Bombers"),
                                 "explosiveDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)