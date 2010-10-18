#Used by:
#Skill: Kinetic Armor Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Armor Hardener",
                                     "passiveKineticDamageResistanceBonus",
                                     skill.getModifiedItemAttr("hardeningbonus2") * skill.level)
