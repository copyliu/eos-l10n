#Items with name like: Ballistic Deflection Field (19 of 19)
#Variations of item: Armor Kinetic Hardener I (39 of 39) [Module]
#Variations of item: Ballistic Deflection Field I (19 of 19) [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("kineticDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))