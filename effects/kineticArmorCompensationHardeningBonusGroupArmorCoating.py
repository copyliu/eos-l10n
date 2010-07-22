#Item: Kinetic Armor Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Coating",
                                  "kineticDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningBonus") * skill.level)