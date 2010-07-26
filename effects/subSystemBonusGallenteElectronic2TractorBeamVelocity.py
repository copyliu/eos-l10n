#Item: Proteus Electronics - Emergent Locus Analyzer [Subsystem]
def handler(fit, module, context):
    level = fit.character.getSkill("Gallente Electronic Systems").level
    fit.modules.filteredItemBoost(lambda mod: mod.group.name == "Tractor Beam",
                                  "maxTractorVelocity", module.getModifiedItemAttr("subsystemBonusGallenteElectronic2") * level)