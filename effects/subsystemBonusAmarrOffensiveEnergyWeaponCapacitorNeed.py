#Item: Legion Offensive - Covert Reconfiguration [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.requiresSkill("Medium Energy Turret"),
                                    "capacitorNeed", module.getModifiedItemAttr("subsystemBonusAmarrOffensive") * level)