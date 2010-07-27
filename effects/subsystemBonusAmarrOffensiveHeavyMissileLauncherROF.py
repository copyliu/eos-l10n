#Item: Legion Offensive - Assault Optimization [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Missile Launcher Heavy",
                                  "speed", module.getModifiedItemAttr("subsystemBonusAmarrOffensive") * level)