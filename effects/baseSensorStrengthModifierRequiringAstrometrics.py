#Items from group: Cyber Science (3 of 30) [Implant]
#Items from group: Cyberimplant (5 of 138) [Implant]
#Items from group: Rig Electronics (6 of 30) [Module]
#Items from group: Scan Probe Launcher (2 of 5) [Module]
#Item: Astrometric Rangefinding [Skill]
def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonus") * level)