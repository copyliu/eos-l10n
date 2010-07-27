#Variations of item: Large Core Defence Operational Solidifier I (2 of 2) [Module]
#Variations of item: Medium Core Defence Operational Solidifier I (2 of 2) [Module]
#Variations of item: Small Core Defence Operational Solidifier I (2 of 2) [Module]
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "duration", module.getModifiedItemAttr("durationSkillBonus"))