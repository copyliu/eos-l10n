#Items with name like: Gravity Capacitor Upgrade (6 of 6)
#Items with name like: Low-grade Virtue (5 of 6)
#Items with name like: Sisters Probe Launcher (2 of 2)
#Items from market group: Implants & Boosters > Implants > Skill Hardwiring > Implant Slot 8 > Science Implants (3 of 8)
#Item: Astrometric Rangefinding [Skill]
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonus") * level)
