#Variations of item: Armor Explosive Hardener I (39 of 39) [Module]
#Variations of item: Explosion Dampening Field I (19 of 19) [Module]
#Item: Civilian Explosion Dampening Field [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("explosiveDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))