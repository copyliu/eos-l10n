#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Science Implants (3 of 6)
#Item: Astrometric Pinpointing [Skill]
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                  "baseMaxScanDeviation", container.getModifiedItemAttr("maxScanDeviationModifier") * level)