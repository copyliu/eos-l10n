#Used by:
#Variations of module: Armor Thermic Hardener I (39 of 39)
#Variations of module: Heat Dissipation Field I (19 of 19)
#Module: Civilian Heat Dissipation Field
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("thermalDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))