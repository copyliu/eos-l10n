#Item: Loki Offensive - Hardpoint Efficiency Configuration [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Missile Launcher Heavy Assault",
                                  "speed", module.getModifiedItemAttr("subsystemBonusMinmatarOffensive") * level)