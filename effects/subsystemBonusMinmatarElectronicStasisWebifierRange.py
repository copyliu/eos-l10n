#Item: Loki Electronics - Immobility Drivers [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Stasis Web",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusMinmatarElectronic") * level)