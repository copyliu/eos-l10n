# Used by:
# Variations of module: Armor EM Hardener I (39 of 39)
# Variations of module: Photon Scattering Field I (19 of 19)
# Module: Civilian Photon Scattering Field
type = "overheat"
def handler(fit, module, context):
    module.boostItemAttr("emDamageResistanceBonus", module.getModifiedItemAttr("overloadHardeningBonus"))