#Item: Thermic Armor Compensation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.group.name == "Armor Hardener",
                                  "passiveThermicDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2"))