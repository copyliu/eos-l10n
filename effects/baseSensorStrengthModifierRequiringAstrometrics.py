#Items from group: Rig Electronics (6 of 30) [Module]
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Science Implants (3 of 8)
#Item: Astrometric Rangefinding [Skill]
#Item: Low-grade Virtue Alpha [Implant]
#Item: Low-grade Virtue Beta [Implant]
#Item: Low-grade Virtue Delta [Implant]
#Item: Low-grade Virtue Epsilon [Implant]
#Item: Low-grade Virtue Gamma [Implant]
#Item: Sisters Core Probe Launcher [Module]
#Item: Sisters Expanded Probe Launcher [Module]
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonus") * level)
