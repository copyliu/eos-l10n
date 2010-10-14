#Used by:
#Skill: Explosive Armor Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Armor Hardener",
                                  "passiveExplosiveDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2") * skill.level)
