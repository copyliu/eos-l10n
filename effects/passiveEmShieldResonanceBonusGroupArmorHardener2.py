# Used by:
# Skill: EM Shield Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Shield Hardener",
                                  "passiveEmDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2") * skill.level)
