#Items from group: Cyber Industry (4 of 19) [Implant]
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 10 > Industry Implants (3 of 9)
#Item: Astrogeology [Skill]
#Item: Mining [Skill]
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Mining"),
                                  "miningAmount", container.getModifiedItemAttr("miningAmountBonus") * level)