#Item: Frequency Modulation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "falloff", skill.getModifiedItemAttr("falloffBonus") * skill.level)