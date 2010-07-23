#Variations of item: Armor Kinetic Hardener I (39 of 39) [Module]
#Variations of item: Ballistic Deflection Field I (19 of 19) [Module]
#Item: Civilian Ballistic Deflection Field [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("kineticDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))