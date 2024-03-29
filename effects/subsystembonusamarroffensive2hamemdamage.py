# Used by:
# Subsystem: Legion Offensive - Assault Optimization
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Assault Missiles"),
                                    "emDamage", module.getModifiedItemAttr("subsystemBonusAmarrOffensive2") * level)
