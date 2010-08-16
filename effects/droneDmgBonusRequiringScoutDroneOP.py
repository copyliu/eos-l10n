#Used by:
#Skill: Combat Drone Operation
type = "passive"
def handler(fit, skill, context):
    for damageType in ("em", "explosive", "kinetic", "thermal"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Scout Drone Operation"),
                                     damageType + "Damage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
