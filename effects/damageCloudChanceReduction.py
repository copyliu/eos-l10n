#Used by:
#Skill: Deep Core Mining
type = "passive"
def handler(fit, skill, context):
    bonus = -skill.getModifiedItemAttr("damageCloudChanceReduction")
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill(skill),
                                     "damageCloudChance", bonus * skill.level)
