#Used by:
#Skills named like: Drone Specialization (4 of 4)
#Skill: Heavy Drone Operation
#Skill: Sentry Drone Interfacing
type = "passive"
def handler(fit, skill, context):
    for damageType in ("em", "explosive", "kinetic", "thermal"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill(skill),
                                     damageType + "Damage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
