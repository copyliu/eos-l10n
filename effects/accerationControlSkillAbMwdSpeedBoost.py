#Item: Acceleration Control [Skill]
#Item: Zor's Custom Navigation Hyper-Link [Implant]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Afterburner",
                                  "speedFactor", container.getModifiedItemAttr("speedFBonus") * level)
