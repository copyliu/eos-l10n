#Used by:
#Skill: Drone Interfacing
type = "passive"
def handler(fit, skill, context):
    for damageType in ("em", "explosive", "kinetic", "thermal"):
        fit.drones.filteredItemBoost(lambda drone: drone.item.requiresSkill("Drones"),
                                     damageType + "Damage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
