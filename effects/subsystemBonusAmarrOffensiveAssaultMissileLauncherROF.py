#Item: Legion Offensive - Assault Optimization [Subsystem]
type = "passive"
def handler(fit, module, context):
    level = fit.character.getSkill("Amarr Offensive Systems").level
    fit.modules.filteredChargeBoost(lambda mod: mod.item.group.name == "Missile Launcher Assault",
                                    "speed", module.getModifiedItemAttr("subsystemBonusAmarrOffensive") * level)
