#Variations of item: Proteus Offensive - Dissonic Encoding Platform (3 of 4) [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Hybrid Turret"),
                                  "damageMultiplier", module.getModifiedItemAttr("subsystemBonusGallenteOffensive2") * level)
