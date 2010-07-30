#Used by:
#Modules named like: Explosion Dampening Field (19 of 19)
#Variations of module: Armor Explosive Hardener I (39 of 39)
#Variations of module: Explosion Dampening Field I (19 of 19)
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("explosiveDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))