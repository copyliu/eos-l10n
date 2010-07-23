#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Missile Implants (3 of 6)
#Variations of item: Large Warhead Rigor Catalyst I (2 of 2) [Module]
#Variations of item: Medium Warhead Rigor Catalyst I (2 of 2) [Module]
#Variations of item: Small Warhead Rigor Catalyst I (2 of 2) [Module]
#Item: Guided Missile Precision [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if context == "skill" else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles") or \
                                                mod.charge.requiresSkill("Heavy Missiles") or \
                                                mod.charge.requiresSkill("Cruise Missiles"),
                                    "aoeCloudSize", container.getModifiedItemAttr("aoeCloudSizeBonus") * level,
                                    stackingPenalties = context != "skill" and context != "implant")