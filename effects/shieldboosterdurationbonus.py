# Used by:
# Modules named like: Core Defense Operational Solidifier (6 of 6)
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Shield Booster",
                                  "duration", module.getModifiedItemAttr("durationSkillBonus"))