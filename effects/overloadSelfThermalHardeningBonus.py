#Items with name like: Heat Dissipation Field (19 of 19)
#Variations of item: Armor Thermic Hardener I (39 of 39) [Module]
#Variations of item: Heat Dissipation Field I (19 of 19) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("thermalDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))