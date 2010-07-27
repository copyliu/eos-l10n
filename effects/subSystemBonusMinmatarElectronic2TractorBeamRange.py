#Item: Loki Electronics - Emergent Locus Analyzer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Minmatar Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Tractor Beam",
                                  "maxRange", module.getModifiedItemAttr("subsystemBonusMinmatarElectronic2") * level)