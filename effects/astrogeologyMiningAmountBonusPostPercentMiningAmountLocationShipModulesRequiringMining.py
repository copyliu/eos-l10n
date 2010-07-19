#Items from group: Cyber Industry (4 of 19) [Implant]
#Item: Astrogeology [Skill]
#Item: Mining [Skill]
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)