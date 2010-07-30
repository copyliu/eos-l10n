#Item: EM Armor Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Plating Energized",
                                  "emDamageResistanceBonus", skill.getModifiedItemAttr("hardeningBonus") * skill.level)
