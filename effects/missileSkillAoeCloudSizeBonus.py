#Items with name like: Warhead Rigor Catalyst (6 of 6)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Missile Implants (3 of 6)
#Item: Guided Missile Precision [Skill]
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Standard Missiles") or \
                                                mod.charge.requiresSkill("Heavy Missiles") or \
                                                mod.charge.requiresSkill("Cruise Missiles"),
                                    "aoeCloudSize", container.getModifiedItemAttr("aoeCloudSizeBonus") * level,
                                    stackingPenalties = "skill" not in context and "implant" not in context)
