#Variations of item: Tengu Offensive - Accelerated Ejection Bay (3 of 4) [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Missile Launcher Heavy",
                                  "speed", module.getModifiedItemAttr("subsystemBonusCaldariOffensive") * level)