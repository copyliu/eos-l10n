#Item: Tengu Electronics - Emergent Locus Analyzer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Caldari Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tractor Beam",
                                  "maxTractorVelocity", module.getModifiedItemAttr("subsystemBonusCaldariElectronic2") * level)