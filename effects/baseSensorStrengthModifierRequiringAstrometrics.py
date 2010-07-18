#Items from group: Cyber Science (3 of 30)
#Items from group: Cyberimplant (5 of 138)
#Items from group: Rig Electronics (6 of 30)
#Items from group: Scan Probe Launcher (2 of 5)
#Item: Astrometric Rangefinding
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonus") * level)