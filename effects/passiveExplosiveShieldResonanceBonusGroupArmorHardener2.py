#Used by:
#Skill: Explosive Shield Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Shield Hardener",
                                     "passiveExplosiveDamageResistanceBonus",
                                     skill.getModifiedItemAttr("hardeningbonus2") * skill.level)
