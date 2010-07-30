#Item: Legion Offensive - Assault Optimization [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                  "thermalDamage", module.getModifiedItemAttr("subsystemBonusAmarrOffensive2") * level)
