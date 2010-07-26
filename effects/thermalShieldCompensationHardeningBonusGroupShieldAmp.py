#Item: Thermic Shield Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Amplifier",
                                  "thermalDamageResistanceBonus", skill.getModifiedItemAttr("hardeningBonus") * skill.level)