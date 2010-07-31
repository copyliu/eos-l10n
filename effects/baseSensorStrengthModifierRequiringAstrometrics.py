#Used by:
#Implants named like: Hardwiring Poteque Pharmaceuticals 'Prospector' PPH (3 of 3)
#Implants named like: Low grade Virtue (5 of 6)
#Modules named like: Gravity Capacitor Upgrade (6 of 6)
#Modules named like: Sisters Probe Launcher (2 of 2)
#Skill: Astrometric Rangefinding
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Astrometrics"),
                                    "baseSensorStrength", container.getModifiedItemAttr("scanStrengthBonus") * level)
