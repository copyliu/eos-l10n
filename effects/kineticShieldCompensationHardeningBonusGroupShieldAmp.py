#Item: Kinetic Shield Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Shield Amplifier",
                                  "kineticDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningBonus") * skill.level)