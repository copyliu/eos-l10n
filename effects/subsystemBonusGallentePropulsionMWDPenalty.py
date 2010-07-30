#Item: Proteus Propulsion - Wake Limiter [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Propulsion Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("High Speed Maneuvering"),
                                    "signatureRadiusBonus", module.getModifiedItemAttr("subsystemBonusGallentePropulsion") * level)
