#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 6 > Science Implants (3 of 6)
#Item: Astrometric Pinpointing [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                  "baseMaxScanDeviation", container.getModifiedItemAttr("maxScanDeviationModifier") * level)
