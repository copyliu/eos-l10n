#Item: Explosive Armor Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Plating Energized",
                                  "explosiveDamageResistanceBonus", skill.getModifiedItemAttr("hardeningBonus") * skill.level)