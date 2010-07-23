#Item: Kinetic Shield Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Shield Hardener",
                                  "passiveKineticDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2"))