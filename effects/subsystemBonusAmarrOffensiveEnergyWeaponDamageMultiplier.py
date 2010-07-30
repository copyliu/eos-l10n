#Item: Legion Offensive - Liquid Crystal Magnifiers [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                    "damageMultiplier", module.getModifiedItemAttr("subsystemBonusAmarrOffensive") * level)
