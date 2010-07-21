#Item: Frequency Modulation [Skill]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tracking Disruptor",
                                  "falloff", skill.getModifiedItemAttr("falloffBonus") * skill.level)