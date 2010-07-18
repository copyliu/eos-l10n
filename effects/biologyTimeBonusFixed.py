#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Science Implants (2 of 8)
#Item: Biology
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.boosters.filteredItemIncrease(lambda: True, "boosterDuration", container.getModifiedItemAttr("durationBonus") * level)