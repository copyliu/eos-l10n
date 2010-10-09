#Used by:
#Skill: Citadel Cruise Missiles
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Citadel Cruise Missiles"),
                                    "thermalDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
