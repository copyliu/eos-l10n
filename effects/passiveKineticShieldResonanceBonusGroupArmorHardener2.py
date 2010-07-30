#Used by:
#Skill: Kinetic Shield Compensation
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.group.name == "Shield Hardener",
                                  "passiveKineticDamageResistanceBonus",
                                  skill.getModifiedItemAttr("hardeningbonus2"))