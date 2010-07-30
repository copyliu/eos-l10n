#Item: Citadel Cruise Missiles [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Citadel Cruise Missiles"),
                                    "thermalDamage", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)