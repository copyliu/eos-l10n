#Used by:
#Modules named like: Ballistic Deflection Field (19 of 19)
#Variations of module: Armor Kinetic Hardener I (39 of 39)
#Variations of module: Ballistic Deflection Field I (19 of 19)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("kineticDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))