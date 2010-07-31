#Used by:
#Subsystem: Legion Offensive - Covert Reconfiguration
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                    "capacitorNeed", module.getModifiedItemAttr("subsystemBonusAmarrOffensive") * level)
