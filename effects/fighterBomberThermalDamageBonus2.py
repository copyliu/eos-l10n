#Used by:
#Skill: Fighter Bombers
type = "passive"
def handler(fit, skill, context):
    fit.drones.filteredChargeBoost(lambda drone: drone.item.requiresSkill("Fighter Bombers"),
                                   "thermalDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
