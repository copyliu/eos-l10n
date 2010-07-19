#Item: Acceleration Control [Skill]
#Item: Zor's Custom Navigation Hyper-Link [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Afterburner",
                                  "speedFactor", container.getModifiedItemAttr("speedFBonus") * level)