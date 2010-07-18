#Items from group: Cyber Industry (4 of 19) [Implant]
#Item: Astrogeology [Skill]
#Item: Mining [Skill]
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)