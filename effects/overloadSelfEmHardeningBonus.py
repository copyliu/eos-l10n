#Variations of item: Armor EM Hardener I (39 of 39) [Module]
#Variations of item: Photon Scattering Field I (19 of 19) [Module]
#Item: Civilian Photon Scattering Field [Module]
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("emDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))