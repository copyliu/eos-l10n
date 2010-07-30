#Used by:
#Modules named like: Heat Dissipation Field (19 of 19)
#Variations of module: Armor Thermic Hardener I (39 of 39)
#Variations of module: Heat Dissipation Field I (19 of 19)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("thermalDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))