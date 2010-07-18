#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Science Implants (3 of 6)
#Item: Astrometric Pinpointing [Skill]
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                  "baseMaxScanDeviation", container.getModifiedItemAttr("maxScanDeviationModifier") * level)