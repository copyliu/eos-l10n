#Used by:
#Variations of module: Armor Explosive Hardener I (39 of 39)
#Variations of module: Explosion Dampening Field I (19 of 19)
#Module: Civilian Explosion Dampening Field
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("explosiveDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))