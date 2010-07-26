#Item: Proteus Offensive - Dissonic Encoding Platform [Subsystem]
#Item: Proteus Offensive - Hybrid Propulsion Armature [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "falloff", module.getModifiedItemAttr("subsystemBonusGallenteOffensive") * level)