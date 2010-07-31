#Used by:
#Skill: EM Armor Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Armor Hardener",
                                  "passiveEmDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2"))