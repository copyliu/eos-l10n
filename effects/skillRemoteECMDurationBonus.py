#Item: Projected Electronic Counter Measures [Skill]
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote ECM Burst",
                                  "duration", skill.getModifiedItemAttr("projECMDurationBonus") * skill.level)