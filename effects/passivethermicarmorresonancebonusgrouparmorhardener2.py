# Used by:
# Skill: Thermic Armor Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Armor Hardener",
                                  "passiveThermicDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2") * skill.level)
