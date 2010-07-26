#Item: Proteus Offensive - Covert Reconfiguration [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", module.getModifiedItemAttr("subsystemBonusGallenteOffensive") * level)