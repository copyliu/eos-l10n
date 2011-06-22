# Used by:
# Implants named like: Hardwiring Poteque Pharmaceuticals 'Prospector' PPF (3 of 3)
# Skill: Astrometric Pinpointing
type = "passive"
def handler(fit, container, context):
    level = container.level if "skill" in context else 1
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Astrometrics"),
                                  "baseMaxScanDeviation", container.getModifiedItemAttr("maxScanDeviationModifier") * level)
