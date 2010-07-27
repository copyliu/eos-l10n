#Item: Tengu Offensive - Rifling Launcher Pattern [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Offensive Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "scanMagnetometricStrengthBonus", module.getModifiedItemAttr("subsystemBonusCaldariOffensive3") * level)