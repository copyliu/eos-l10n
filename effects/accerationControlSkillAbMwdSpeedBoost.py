#Item: Acceleration Control [Skill]
#Item: Zor's Custom Navigation Hyper-Link [Implant]
type = "passive"
def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Afterburner",
                                  "speedFactor", skill.getModifiedItemAttr("speedFBonus") * skill.level)