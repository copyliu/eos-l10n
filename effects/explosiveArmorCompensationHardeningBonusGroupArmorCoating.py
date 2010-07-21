#Item: Explosive Armor Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Armor Coating",
                                  "explosiveDamageResistanceBonus", skill.getModifiedItemAttr("hardeningBonus") * skill.level)