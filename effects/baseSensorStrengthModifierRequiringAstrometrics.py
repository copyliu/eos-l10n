def handler(fit, container, context):
    if context == "skill": level = container.level
    else: level = 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonus") * level)